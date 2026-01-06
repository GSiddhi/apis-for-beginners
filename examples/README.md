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

In simple terms, you are pretending to be an external service (such as Stripe or GitHub) and sending a webhook event to your application.

