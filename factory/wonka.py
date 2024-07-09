import json
import random
import time
from kafka import KafkaProducer

# Kafka configuration
KAFKA_BROKER = 'localhost:9092'  # Change this to your Kafka broker address
TOPIC = 'candies'

# Candy data
candy_types = ['chocolate', 'gummy', 'hard', 'lollipop', 'marshmallow', 'fizzy', 'sour']
candies = {
    'chocolate': ['Wonka Bar', 'Chocolate River Delight', 'Golden Ticket Truffle'],
    'gummy': ['Everlasting Gobstopper', 'Fizzy Lifting Gummy', 'Whipple-Scrumptious FudgeMallow Delight'],
    'hard': ['Scrumdiddlyumptious Jawbreaker', 'Butterscotch Blast', 'Peppermint Creams'],
    'lollipop': ['Rainbow Drop Lollipop', 'Fizzing Whizbee Pop', 'Juicy Bubble Lick'],
    'marshmallow': ['Marshmallow Pillows', 'Fluffy Whip', 'Marshmallow Clouds'],
    'fizzy': ['Fizzy Lifting Drink', 'Bubbling Bonbons', 'Sparkling Sherbet'],
    'sour': ['Sour Schnozzberries', 'Tangy Tongue Twisters', 'Zingy Zapple Zaps']
}

def generate_candy_data():
    candy_type = random.choice(candy_types)
    candy_name = random.choice(candies[candy_type])
    return {
        "type": candy_type,
        "candy": candy_name
    }

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        batch_size=16384,       # 16KB batch size 
        linger_ms=10            # 10ms linger time
    )

    try:
        while True:
            candy_data = generate_candy_data()
            producer.send(TOPIC, candy_data)
            print(f'Produced: {candy_data}')
            time.sleep(1)  # Adjust the sleep time as needed

    except KeyboardInterrupt:
        print('Stopping producer...')
    finally:
        producer.close()

if __name__ == '__main__':
    main()
