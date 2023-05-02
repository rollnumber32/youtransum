document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("summarize")
    .addEventListener("click", async function () {
      const [tab] = await chrome.tabs.query({
        currentWindow: true,
        active: true,
      });
      chrome.tabs.sendMessage(tab.id, {
        action: "generate",
        url: tab.url,
      });
    });
});

chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === "summary") {
    const summary_div = document.getElementById("summary");
    summary_div.innerHTML = message.content;
  }
});
