function DeckConstructor() {
    var suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds'];
    var values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'];
    var deck;

    this.show = function(){
        console.log(deck);
        console.log('Length:', deck.length);
        return this;
    }

    var generateDeck = function(){
        deck = []
        for (var i = 0; i < suits.length; i++){
            for (var j = 0; j < values.length; j++){
                // var card = {};
                // card.suit = suits[i]; // can also do card['suit'], we're setting the keys
                // card.value = values[j]; // also setting keys here
                var card = new Card(suits[i], values[j]);
                deck.push(card);
            }
        }
    }
    generateDeck();

    this.shuffle = function(){
        var numberOfShuffles = Math.floor((Math.random() * 100) + 50);
        for (var i = 0; i <= numberOfShuffles; i++){
            var randomInteger1 = Math.floor(Math.random() * deck.length);
            var randomInteger2 = Math.floor(Math.random() * deck.length);
            // perform basic swap
            var temp = deck[randomInteger1];
            deck[randomInteger1] = deck[randomInteger2];
            deck[randomInteger2] = temp;
        }
        return this; // the whole deck object
    }
    this.reset = generateDeck;

    this.getDeck = function(){ // did this for prototype to work
        return deck;
    }
}

DeckConstructor.prototype.deal = function(){
    return this.getDeck().pop();
}

// Card Constructor
function Card(suit, value){
    // var card = {} <- would need if we didn't have the 'this'
    this.suit = suit;
    this.value = value;
}

var myDeck = new DeckConstructor();

myDeck.shuffle().reset();

myDeck.shuffle();

myDeck.show();

console.log(myDeck.deal());
