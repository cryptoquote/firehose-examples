
# CryptoQuote Firehose for NodeJS

Injest full firehose using NodeJS in just a few lines.

Contact devs@cryptoquote.io for your credentials.

Sign up for a free account here: https://cryptoquote.io

### Installing

```
npm install
```

```js
'use strict';

const nats = require('nats');

let natsHost = process.env.NATS_HOST || 'nats-01.cryptoquote.io';

const nc = nats.connect(`nats://username:pass@${natsHost}`);

let exchange = process.argv[2] || 'gdax';

console.log('Listening for all of', exchange, 'ON', natsHost);

setTimeout(() => {
    nc.subscribe(`hose.*.${exchange}.>`, function (msg) {
        console.log('Received a message: ' + msg);
    });
}, 1500);
```