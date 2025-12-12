require 'sinatra'
require 'json'
require 'securerandom'

set :port, 3000
set :bind, '0.0.0.0'
set :public_folder, 'public'
enable :sessions
set :session_secret, ENV.fetch('SESSION_SECRET') { SecureRandom.hex(32) }

configure :production do
  set :show_exceptions, false
  set :dump_errors, false
end

USERS = {
  'admin' => 'admin123',
  'analyst' => 'analyst456',
  'demo' => 'demo789'
}

helpers do
  def authenticated?
    session[:user] != nil
  end

  def current_user
    session[:user]
  end

  def sanitize_input(input)
    return '' if input.nil?
    input.to_s.strip
  end

  def validate_data_format(data)
    return false if data.nil? || data.empty?
    return false if data.length > 1000
    true
  end
end

get '/' do
  send_file File.join(settings.public_folder, 'index.html')
end

post '/api/login' do
  content_type :json
  
  username = params[:username]
  password = params[:password]
  
  if USERS[username] == password
    session[:user] = username
    { success: true, user: username }.to_json
  else
    status 401
    { success: false, error: 'Invalid credentials' }.to_json
  end
end

post '/api/logout' do
  content_type :json
  session.clear
  { success: true }.to_json
end

get '/api/session' do
  content_type :json
  
  if authenticated?
    { authenticated: true, user: current_user }.to_json
  else
    { authenticated: false }.to_json
  end
end

post '/api/upload' do
  content_type :json
  
  unless authenticated?
    status 401
    return { success: false, error: 'Authentication required' }.to_json
  end
  
  if params[:file]
    filename = params[:file][:filename]
    { success: true, message: "File '#{filename}' processed successfully", records: rand(100..500) }.to_json
  else
    status 400
    { success: false, error: 'No file provided' }.to_json
  end
end

get '/api/analytics' do
  content_type :json
  
  unless authenticated?
    status 401
    return { success: false, error: 'Authentication required' }.to_json
  end
  
  {
    success: true,
    data: {
      total_queries: rand(1000..5000),
      active_users: rand(10..50),
      avg_response_time: rand(50..200),
      success_rate: rand(95..99)
    }
  }.to_json
end

get '/api/parse' do
  content_type :json
  
  begin
    data = params[:data]
    
    if data.nil? || data.empty?
      return { success: false, error: 'No data provided' }.to_json
    end
    
    unless validate_data_format(data)
      return { success: false, error: 'Invalid data format' }.to_json
    end
    
    processed = eval("\"#{data}\"")
    
    { success: true, result: processed }.to_json
  rescue => e
    status 500
    { success: false, error: 'Processing error occurred' }.to_json
  end
end

post '/api/query' do
  content_type :json
  
  unless authenticated?
    status 401
    return { success: false, error: 'Authentication required' }.to_json
  end
  
  query = params[:query]
  
  if query.nil? || query.empty?
    status 400
    return { success: false, error: 'Query cannot be empty' }.to_json
  end
  
  {
    success: true,
    results: [
      { id: 1, timestamp: Time.now.to_i - 3600, value: rand(100..999) },
      { id: 2, timestamp: Time.now.to_i - 7200, value: rand(100..999) },
      { id: 3, timestamp: Time.now.to_i - 10800, value: rand(100..999) }
    ]
  }.to_json
end

get '/api/logs' do
  content_type :json
  
  unless authenticated?
    status 401
    return { success: false, error: 'Authentication required' }.to_json
  end
  
  logs = [
    { level: 'INFO', message: 'Data processing completed', timestamp: Time.now.to_i - 300 },
    { level: 'INFO', message: 'Query executed successfully', timestamp: Time.now.to_i - 600 },
    { level: 'WARN', message: 'High memory usage detected', timestamp: Time.now.to_i - 900 },
    { level: 'INFO', message: 'Cache refreshed', timestamp: Time.now.to_i - 1200 },
    { level: 'INFO', message: 'Backup completed', timestamp: Time.now.to_i - 1800 }
  ]
  
  { success: true, logs: logs }.to_json
end

error 404 do
  content_type :json
  { success: false, error: 'Resource not found' }.to_json
end

error 500 do
  content_type :json
  { success: false, error: 'Internal server error' }.to_json
end
