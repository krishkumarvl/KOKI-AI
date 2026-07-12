// app.js — KOKI Web UI

const chatArea = document.getElementById('chatArea');
const msgInput = document.getElementById('msgInput');

// ── Add message to chat ──
function addMessage(text, sender) {
  const wrapper = document.createElement('div');
  wrapper.className = sender === 'user' ? 'user-msg' : 'koki-msg';

  const bubble = document.createElement('div');
  bubble.className = `msg-bubble ${sender}`;
  bubble.textContent = text;

  wrapper.appendChild(bubble);
  chatArea.appendChild(wrapper);
  chatArea.scrollTop = chatArea.scrollHeight;
}

// ── Typing indicator ──
function showTyping() {
  const wrapper = document.createElement('div');
  wrapper.className = 'koki-msg';
  wrapper.id = 'typingIndicator';

  wrapper.innerHTML = `
    <div class="typing-indicator">
      <span></span><span></span><span></span>
    </div>
  `;
  chatArea.appendChild(wrapper);
  chatArea.scrollTop = chatArea.scrollHeight;
}

function hideTyping() {
  const indicator = document.getElementById('typingIndicator');
  if (indicator) indicator.remove();
}

// ── Send message ──
async function sendMessage() {
  const msg = msgInput.value.trim();
  if (!msg) return;

  addMessage(msg, 'user');
  msgInput.value = '';
  showTyping();

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg })
    });

    const data = await res.json();
    hideTyping();
    addMessage(data.reply, 'koki');

  } catch (err) {
    hideTyping();
    addMessage('Connection error — try again.', 'koki');
  }
}

// ── Quick command buttons ──
function quickSend(prefix) {
  msgInput.value = prefix;
  msgInput.focus();
}

// ── Save name from modal ──
async function saveName() {
  const name = document.getElementById('nameInput').value.trim();
  if (!name) return;

  await fetch('/set-name', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: name })
  });

  document.getElementById('nameModal').style.display = 'none';
  document.getElementById('app').style.display = 'grid';
  document.getElementById('sidebarName').textContent = name;

  addMessage(`Namaste ${name}! Main KOKI hoon — tera personal AI. Kya baat karein aaj? 🙏`, 'koki');
}

// ── Enter key ──
msgInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendMessage();
});

// ── Enter key in name modal ──
const nameInput = document.getElementById('nameInput');
if (nameInput) {
  nameInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') saveName();
  });
}