let globalState = {
    tools: [],
    tokenCountIndented: 0,
    tokenCountCompact: 0
};

let isToolsIndented = true;

async function fetchData() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();

        if (window.getSelection().toString().length > 0) return;

        globalState.tools = data.tools_defined;
        globalState.tokenCountIndented = data.tools_tokens_indented;
        globalState.tokenCountCompact = data.tools_tokens_compact;

        document.getElementById('sys-prompt').innerText = data.latest_system_prompt;
        document.getElementById('sys-tokens').innerText = data.system_prompt_tokens + " tokens";

        document.getElementById('user-prompt').innerText = data.latest_user_prompt;
        document.getElementById('user-tokens').innerText = data.user_prompt_tokens + " tokens";

        document.getElementById('model-name').innerText = data.model_requested;
        document.getElementById('ts').innerText = data.timestamp;

        renderTools();
    } catch (e) {
        console.error(e);
    }
}

function renderTools() {
    const toolsBox = document.getElementById('tools-display');
    const tokensBadge = document.getElementById('tool-tokens');

    if (!globalState.tools || globalState.tools.length === 0) {
        toolsBox.innerText = "// No tools provided in request";
        tokensBadge.innerText = "0 tokens";
        return;
    }

    if (isToolsIndented) {
        toolsBox.innerText = JSON.stringify(globalState.tools, null, 2);
        tokensBadge.innerText = globalState.tokenCountIndented + " tokens (Indented)";
    } else {
        toolsBox.innerText = JSON.stringify(globalState.tools);
        tokensBadge.innerText = globalState.tokenCountCompact + " tokens (Compact)";
    }
}

function toggleToolsFormat() {
    const checkbox = document.getElementById('tools-toggle');
    isToolsIndented = checkbox.checked;
    renderTools();
}

setInterval(fetchData, 1000);

async function copyContent(elementId, btn) {
    const text = document.getElementById(elementId).innerText;
    const originalText = btn.innerHTML;

    try {
        await navigator.clipboard.writeText(text);
        btn.classList.add('success');
        btn.innerText = "✅ Copied!";
        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.classList.remove('success');
        }, 2000);
    } catch (err) {
        console.error("Clipboard error:", err);
        if (err.name === 'NotAllowedError') {
            alert("Clipboard access denied. Ensure you're using HTTPS or localhost.");
        } else {
            alert("Failed to copy to clipboard: " + err.message);
        }
    }
}
