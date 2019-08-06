
# CryptoQuote Firehose for Java

Injest full firehose using Java in just a few lines.

Contact devs@cryptoquote.io for your credentials.

Sign up for a free account here: https://cryptoquote.io

### Installing

```xml
<dependency>
    <groupId>io.nats</groupId>
    <artifactId>jnats</artifactId>
    <version>2.5.0</version>
</dependency>
```

```java
package main;

import java.nio.charset.StandardCharsets;

import com.google.gson.Gson;

import io.nats.client.Connection;
import io.nats.client.Dispatcher;
import io.nats.client.Nats;

class Message {
	public String updateType;
	public String symbol;
	public long updated;

	public String toString() {
		return symbol + " updated at " + updated + " for event " + updateType;
	}
}

public class Firehose {

	public static void main(String... a) {
		try {
			Connection nc = Nats.connect("nats://user:secret@nats-01.cryptoquote.io");
			Gson gson = new Gson();
			
			// Create a dispatcher and inline message handler
			Dispatcher d = nc.createDispatcher((msg) -> {
				
				String json = new String(msg.getData(), StandardCharsets.UTF_8);
				Message updateMsg = gson.fromJson(json, Message.class);

				// Use the object
				System.out.println(updateMsg);
			});

			// Subscribe to all trades
			d.subscribe("hose.trade.>");

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
```