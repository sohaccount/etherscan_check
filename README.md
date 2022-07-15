# 流れ

①Twilioで電話番号購入、APIキーの発行  
②etherscanでAPIキーの発行  
③Google cloud functionの設定※他のサービスでも可能ですがコードは修正しないといけない可能性あります。  


# 実行されること

Dooarアドレスに addLiquidity があった場合に指定した電話番号に電話する。  
eGSTのオーナーアドレスがmintした場合に電話番号に電話する。
Google Cloud Functionは1分毎に呼び出されるが、念のため現在時刻から2分前までのトランザクションを対象とする。  
※条件判定にaddLiquidity(address tokenA, address tokenB, uint256 amountADesired, uint256 amountBDesired, uint256 amountAMin, uint256 amountBMin, address to, uint256 deadline)と一致を指定しているので、それ以外の記載のパターンがあった場合は検知できません。


# Twilio電話番号取得とAPIkeyの取得
https://cloudapi.kddi-web.com/magazine/twilio-lesson/how-to-buy-a-telephone-number


# Google cloud functionの設定流れ
https://note.com/10mohi6/n/naa1d4ee3d3bf


その他迷いそうなところ

エントリポイント  
add_liqudity_check  

Cloud Schedulerの頻度部分  
\* \* \* \* \*



# 環境変数は以下を設定ください 　 

account_sid　#twilio  
auth_token #twilio  
etherscan_api #etherscan_api  
discord_webhooks #discord ※使いたい場合のみ  
to #自分の電話番号　+81から記載　例）090-9999-9999の場合　+819099999999  
from　#twilioで作った電話番号　+81から記載　※上記参照  
address #監視対象のアドレス　eGSTのDooarアドレスの場合　0x53e0e51b5Ed9202110D7Ecd637A4581db8b9879F  
owner_address　#オーナーアドレス　0x6238872A0Bd9F0E19073695532a7Ed77ce93C69E

