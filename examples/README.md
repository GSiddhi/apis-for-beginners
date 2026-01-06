## Testing the webhook (Windows PowerShell)

Use Invoke-RestMethod:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/webhook `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"event":"order_created","order_id":123}'
```

### What this command does

This command manually sends a webhook event to your local webhook server to verify that:

- the server is running  
- it can receive POST requests  
- it can read JSON data  
- it responds correctly  

In simple terms, you are pretending to be an external service and sending a webhook event to your application.

---

## WebRTC Example

The WebRTC example runs in a web browser, not from the terminal.

### How to run

1. Open the folder containing `webrtc_example.html` in VS Code  
2. Right-click the file and choose **Open with Live Server**  
   (or open the file directly in a browser)
3. Allow camera access when prompted

You should see your live camera feed in the browser.
