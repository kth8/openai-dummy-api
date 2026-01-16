DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>OpenAI Dummy API</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="/static/css/dashboard.css">
</head>
<body>
    <div class="container">
        <h1>🕵️ OpenAI Dummy API</h1>

        <div class="meta">
            <span>Model: <span id="model-name" class="badge">Waiting...</span></span>
            <span>Last Request: <span id="ts" style="color: #fff">--</span></span>
        </div>

        <div class="card">
            <div class="card-header">
                <div class="header-left">
                    <h3>📜 System Prompt</h3>
                    <span id="sys-tokens" class="token-badge">0 tokens</span>
                </div>
                <button class="copy-btn" onclick="copyContent('sys-prompt', this)">
                    <i class="fas fa-copy"></i> Copy
                </button>
            </div>
            <div id="sys-prompt" class="code-box">Waiting for request...</div>
        </div>

        <div class="card">
            <div class="card-header">
                <div class="header-left">
                    <h3>👤 User Prompt</h3>
                    <span id="user-tokens" class="token-badge">0 tokens</span>
                </div>
                <button class="copy-btn" onclick="copyContent('user-prompt', this)">
                    <i class="fas fa-copy"></i> Copy
                </button>
            </div>
            <div id="user-prompt" class="code-box user-box">Waiting for request...</div>
        </div>

        <div class="card">
            <div class="card-header">
                <div class="header-left">
                    <h3>🛠️ Tool Definitions</h3>
                    <span id="tool-tokens" class="token-badge">0 tokens</span>
                    <div class="toggle-wrapper" style="margin-left: 10px;">
                        <span>Compact</span>
                        <label class="switch">
                            <input type="checkbox" id="tools-toggle" checked onclick="toggleToolsFormat()">
                            <span class="slider"></span>
                        </label>
                        <span>Indented</span>
                    </div>
                </div>
                <button class="copy-btn" onclick="copyContent('tools-display', this)">
                    <i class="fas fa-copy"></i> Copy
                </button>
            </div>
            <div id="tools-display" class="code-box tools-box">// Waiting for request with tools...</div>
        </div>
    </div>
    <script src="/static/js/dashboard.js"></script>
</body>
</html>
"""
