
# CryptoQuote Firehose for Golang

Injest full firehose using Golang in just a few lines.

Contact devs@cryptoquote.io for your credentials.

Sign up for a free account here: https://cryptoquote.io


```bash
$ go get github.com/nats-io/nats.go/
```

```go
package main

import (
	"fmt"

	nats "github.com/nats-io/nats.go"
)

func main() {
	// Connect to a server
	nc, _ := nats.Connect("nats://username:password@nats-01.cryptoquote.io:4222")

	// Simple Async Subscriber
	nc.Subscribe("hose.trade.>", func(m *nats.Msg) {
		fmt.Printf("Received a Trade: %s\n", string(m.Data))
	})

	// block
	chann := make(chan struct{})
	<-chann

}
```