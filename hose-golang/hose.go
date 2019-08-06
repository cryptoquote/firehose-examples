package main

import (
	"fmt"

	nats "github.com/nats-io/nats.go"
)

func main() {
	// Connect to a server
	nc, _ := nats.Connect("nats://firehose:GXtU*!igBv@nats-01.cryptoquote.io:4222")

	// Simple Async Subscriber
	nc.Subscribe("hose.trade.>", func(m *nats.Msg) {
		fmt.Printf("Received a Trade: %s\n", string(m.Data))
	})

	// block
	chann := make(chan struct{})
	<-chann
}
