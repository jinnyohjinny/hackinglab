FROM ruby:2.7-alpine

WORKDIR /app

RUN apk add --no-cache build-base

COPY Gemfile ./
RUN bundle install --without development test

COPY . .

EXPOSE 3000

ENV RACK_ENV=production

CMD ["ruby", "app.rb"]
