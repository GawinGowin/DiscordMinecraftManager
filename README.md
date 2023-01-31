# DiscordMinecraftManager
EC2インスタンス上に実装したMinecraftServerのDiscordBotを用いた起動/停止アプリケーション

## 前提
- Discordを介した基本身内でのMinecraftのマルチプレイ環境
- EC2インスタンスの起動/停止時に自動的にMinecraftServerが起動する設定

![SS](https://user-images.githubusercontent.com/101625248/215903524-52c03bd8-50ba-454e-8c4b-aaacbf2b3f34.png)

## コンフィグファイルの説明
-> [config.json](/.devcontainer/config.json)

**Discord関係**
>- bot_token : DiscordのBotアカウントのトークン
>- channel_id : DiscordサーバーにこのBotを招待した時，スラッシュコマンドが有効なチャンネルのID

**AWS関係**
>- aws_access_key_id : 制御に用いるIAM ユーザーのアクセスキー
>- aws_secret_access_key : そのシークレットキー
>- region_name: 接続時のゾーン
>- server_instance_id: MinecraftServerをデプロイしているEC2インスタンスのID

・コンフィグファイルにクレデンシャル情報を記述しているので，セキュリティ上の懸念が残る．
