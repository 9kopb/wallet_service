from sanic import Sanic
from sanic.response import text, json
from electrum_cmd_util import APICmdUtil

app = Sanic("BlockonomicsWalletServiceAPI")

@app.post("/api/presend")
async def presend(request):
  args = request.json
  addr = args.get('addr')
  btc_amount = args.get('btc_amount')
  wallet_id = args.get('wallet_id')
  wallet_password = args.get('wallet_password')
  api_password = args.get('api_password')

  estimated_fee = await APICmdUtil.presend(addr, btc_amount, wallet_id, wallet_password, api_password)
  return json({"estimated_fee": estimated_fee})

@app.post("/api/send")
async def send(request):
  args = request.json
  addr = args.get('addr')
  btc_amount = args.get('btc_amount')
  wallet_id = args.get('wallet_id')
  wallet_password = args.get('wallet_password')
  api_password = args.get('api_password')
  
  estimated_fee, internal_txid = await APICmdUtil.send(addr, btc_amount, wallet_id, wallet_password, api_password)
  return json({"estimated_fee": estimated_fee, "internal_txid": internal_txid})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)