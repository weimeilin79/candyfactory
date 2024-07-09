package main

import (
	"encoding/json"
	"math/rand"
	"time"
	"github.com/redpanda-data/redpanda/src/transform-sdk/go/transform"
)

func main() {
	// Register your transform function.
	// This is a good place to perform other setup too.
	transform.OnRecordWritten(doTransform)

	// Seed the random number generator
	rand.Seed(time.Now().UnixNano())
}

// doTransform is where you read the record that was written, and then you can
// output new records that will be written to the destination topic
func doTransform(e transform.WriteEvent, w transform.RecordWriter) error {
	// Unmarshal the JSON payload
	var payload map[string]interface{}
	err := json.Unmarshal(e.Record().Value, &payload)
	if err != nil {
		return err
	}

	// Randomly (1/10) add a "hasGoldenTicket" field to the JSON payload
	if rand.Intn(10) == 0 {
		payload["hasGoldenTicket"] = true
	} else {
		payload["hasGoldenTicket"] = false
	}

	// Marshal the modified payload back to JSON
	modifiedValue, err := json.Marshal(payload)
	if err != nil {
		return err
	}

	// Write the modified record
	return w.Write(transform.Record{
		Key:   e.Record().Key,
		Value: modifiedValue,
	})
}
