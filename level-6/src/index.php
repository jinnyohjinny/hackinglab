<?php
error_reporting(0);

$result = '';
$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST' || !empty($_GET['message'])) {
    $message = isset($_POST['message']) ? $_POST['message'] : (isset($_GET['message']) ? $_GET['message'] : '');
    $pattern = isset($_POST['pattern']) ? $_POST['pattern'] : (isset($_GET['pattern']) ? $_GET['pattern'] : '');
    $new = isset($_POST['new']) ? $_POST['new'] : (isset($_GET['new']) ? $_GET['new'] : '');
    
    if (empty($message)) {
        $error = 'Please provide a message to transform.';
    } elseif (empty($pattern)) {
        $error = 'Please provide a pattern to match.';
    } elseif (!isset($new)) {
        $error = 'Please provide a replacement value.';
    } else {
        if (preg_match('/^\/.*\/[a-z]*$/i', $pattern)) {
            if (!preg_match('/e/', $pattern)) {
                $pattern = rtrim($pattern, '/') . 'e/';
            }
        }
        
        $result = @preg_replace($pattern, $new, $message);
        
        if ($result === null) {
            $error = 'Invalid pattern provided. Please check your pattern syntax.';
            $result = '';
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Transformer - Advanced Pattern Replacement Tool</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>✨ Text Transformer</h1>
            <p>Advanced pattern-based text transformation utility</p>
        </div>

        <div class="card">
            <div class="info-box">
                <p><strong>How to use:</strong> Enter your text message, define a pattern to match, and specify the replacement value.</p>
                <p><strong>Pattern examples:</strong> Use simple text (e.g., "hello") or regex patterns (e.g., "/[0-9]+/" to match numbers)</p>
            </div>

            <form method="POST" action="">
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea name="message" id="message" class="form-control" placeholder="Enter your text message here..."><?php echo htmlspecialchars(isset($_POST['message']) ? $_POST['message'] : ''); ?></textarea>
                </div>

                <div class="form-group">
                    <label for="pattern">Pattern to Match</label>
                    <input type="text" name="pattern" id="pattern" class="form-control" placeholder="e.g., /world/i or simple text" value="<?php echo htmlspecialchars(isset($_POST['pattern']) ? $_POST['pattern'] : ''); ?>">
                </div>

                <div class="form-group">
                    <label for="new">Replacement Value</label>
                    <input type="text" name="new" id="new" class="form-control" placeholder="Enter replacement text" value="<?php echo htmlspecialchars(isset($_POST['new']) ? $_POST['new'] : ''); ?>">
                </div>

                <button type="submit" class="btn">Transform Text</button>
            </form>
        </div>

        <?php if ($error): ?>
        <div class="card">
            <div style="background: #fee2e2; border-left: 4px solid #ef4444; padding: 15px; border-radius: 8px;">
                <p style="color: #991b1b; margin: 0;"><strong>Error:</strong> <?php echo htmlspecialchars($error); ?></p>
            </div>
        </div>
        <?php endif; ?>

        <?php if ($result !== '' && !$error): ?>
        <div class="card">
            <div class="result-box">
                <h3>✓ Transformation Complete</h3>
                <div class="result-content"><?php echo $result; ?></div>
            </div>
        </div>
        <?php endif; ?>

        <div class="footer">
            <p>Text Transformer v1.0 | Professional Text Processing Tool</p>
        </div>
    </div>
</body>
</html>
