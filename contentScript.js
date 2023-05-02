chrome.runtime.onMessage.addListener(async function (
  request,
  sender,
  sendResponse
) {
  if (request.action === "generate") {
    const url = new URL(request.url);
    const video_id = url.searchParams.get("v");
    response = await fetch(
      `http://localhost:8000/api/summarize/${video_id}`
    ).then((resp) => resp.text());
    chrome.runtime.sendMessage({ action: "summary", content: response });
  }
});
