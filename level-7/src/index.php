<?php
error_reporting(0);
ini_set('display_errors', 0);
assert_options(ASSERT_ACTIVE, 1);
assert_options(ASSERT_WARNING, 0);
assert_options(ASSERT_BAIL, 0);

$output = '';
$status = '';

function validateExpression($expr) {
    if (empty($expr)) {
        return ['valid' => false, 'message' => 'Expression cannot be empty'];
    }
    
    if (strlen($expr) > 200) {
        return ['valid' => false, 'message' => 'Expression too long'];
    }
    
    return ['valid' => true, 'message' => 'Expression validated successfully'];
}

if (isset($_GET['expr'])) {
    $expr = $_GET['expr'];
    
    $validation = validateExpression($expr);
    
    if ($validation['valid']) {
        $check = assert($expr);
        
        if ($check !== false) {
            $status = 'success';
            $output = 'Expression evaluated successfully. Result: Valid';
        } else {
            $status = 'warning';
            $output = 'Expression evaluated but returned false';
        }
    } else {
        $status = 'error';
        $output = $validation['message'];
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expression Validator - Professional Logic Testing Tool</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Expression Validator</h1>
            <p>Professional logical expression testing and validation utility</p>
        </div>

        <div class="card">
            <div class="info-box">
                <p><strong>About this tool:</strong> Test and validate logical expressions to ensure they evaluate correctly.</p>
                <p><strong>Examples:</strong> Try expressions like <code>1==1</code>, <code>true</code>, <code>'hello'=='hello'</code>, or <code>5>3</code></p>
            </div>

            <form method="GET" action="">
                <div class="form-group">
                    <label for="expr">Expression to Validate</label>
                    <input type="text" name="expr" id="expr" class="form-control" placeholder="Enter a logical expression (e.g., 1==1)" value="<?php echo htmlspecialchars(isset($_GET['expr']) ? $_GET['expr'] : ''); ?>">
                </div>

                <button type="submit" class="btn">Validate Expression</button>
            </form>
        </div>

        <?php if ($status === 'error'): ?>
        <div class="card">
            <div class="alert alert-error">
                <strong>Validation Error:</strong> <?php echo htmlspecialchars($output); ?>
            </div>
        </div>
        <?php endif; ?>

        <?php if ($status === 'success'): ?>
        <div class="card">
            <div class="alert alert-success">
                <strong>✓ Success:</strong> <?php echo htmlspecialchars($output); ?>
            </div>
        </div>
        <?php endif; ?>

        <?php if ($status === 'warning'): ?>
        <div class="card">
            <div class="alert alert-warning">
                <strong>⚠ Notice:</strong> <?php echo htmlspecialchars($output); ?>
            </div>
        </div>
        <?php endif; ?>

        <div class="footer">
            <p>Expression Validator v1.0 | Enterprise Logic Testing Platform</p>
        </div>
    </div>
</body>
</html>
