# Auto poster for discord.

## Description
> - ini sebenarnya adalah program yang non legal jadi segala masalah yang terjadi pada akun anda bukan tanggung jawabku
>
> - menggunakan berarti berarti siap menerima semua resiko seperti account banned dll

## Package Required
> - pastiin udah install python ya kusaranin juga make python new version atau yang terbaru
>
> - package wajib update dan upgrade dulu ya njer:v
>
> - udah kukasi `requirements.txt` jadi gaperlu install" lagi cukup py aja

## Installation and setup
> - clone aja ni repository dengan cara `git clone https://github.com/Yasurooo/Posted-discord.git` dan tunggu sampe clonenya done
>
> - masuk ke directory dengan cara `cd Poster-discord`
>
> - setelah masuk kedalam kan ada file `config.json` nah itu diedit ajah ya editnya bisa package nano atau make code editor yah
>
>  - kalo udah ya run lah:v make `python main.py`
>

## Structure JSON
```json
{
    "TOKEN": "TOKEN_IN_HERE",
    "CHANNELS": [
        {
            "id": "ID_CHANNEL",
            "delay": 0,
            "message": "MESSAGE_IN_HERE",
            "use_config_delay": false
        }
    ],
    "LOG_WEBHOOK_URL": "WEBHOOK_URL",
    "EMOJIS": {
        "Status_Emoji": "EMOJI_HERE",
        "Uptime_Emoji": "EMOJI_HERE",
        "Channel_Emoji": "EMOJI_HERE",
        "Logs_Emoji": "EMOJI_HERE",
        "Message_Emoji": "EMOJI_HERE"
    },
    "ENABLE_LOOP": true
}
```
