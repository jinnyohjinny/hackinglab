import urllib.parse

class SecurityFilter:
    """
    Advanced security filtering for code analysis requests.
    Implements multi-layer validation to prevent malicious input.
    """
    
    BLOCKED_PATTERNS = ['/']
    
    @staticmethod
    def validate_input(code_snippet):
        """
        Validates code snippet against security rules.
        
        Args:
            code_snippet: The code to validate
            
        Returns:
            tuple: (is_valid, error_message, decoded_code)
        """
        if not code_snippet:
            return False, "Code snippet cannot be empty", None
            
        if any(pattern in code_snippet for pattern in SecurityFilter.BLOCKED_PATTERNS):
            return False, "Invalid character detected in input", None
        
        decoded = urllib.parse.unquote(code_snippet)
        
        if any(pattern in decoded for pattern in SecurityFilter.BLOCKED_PATTERNS):
            return False, "Security violation: Suspicious pattern detected", None
        
        return True, None, decoded
    
    @staticmethod
    def sanitize_output(output):
        """
        Sanitizes output to prevent information disclosure.
        
        Args:
            output: Raw output from analysis
            
        Returns:
            str: Sanitized output
        """
        if len(output) > 1000:
            return output[:1000] + "... (truncated)"
        return output
