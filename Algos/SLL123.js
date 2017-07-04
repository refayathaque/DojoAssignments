function Node(value) {
    this.val = value;
    this.next = null;
    }

function SLL() {
    this.head = null;

    this.insert = function(val) {
        if(!this.head) {
            this.head = new Node(val)
            return this.head;
        }
        var current = this.head; // allows us to TRAVERSE through list (NOT ITERATE)
        while(current.next) {
        current = current.next;
        }
        current.next = new Node(val)
        return this.head
    }

    this.splitOnVal = function(list, val) {
        if(!this.head) {
            console.log("You can't split on an empty list")
            return this.head
        }
        var current = this.head.next
        var previous = this.head
        if(previous.val === val) {
            list.head = previous;
            this.head = null
            return list.head;
        }
        while(current) {
            if(current.val === val) {
                list.head = current
                previous.next = null
                return list.head
            }
            current = current.next
            previous = previous.next
         }
         return list.head
    }

    this.shiftRight = function(list, shiftby) {
        for (var i = 0; i <= shiftby; i++) {
            var first = this.head;
            var p = this.head;
            var c = this.head.next;
            while (c.next) {
                c = c.next;
                p = p.next;
            }
            p.next = null;
            this.head=c;
            c.next = first;
        }
        return list;
    }

}

var list1 = new SLL()

list1.insert(1)
list1.insert(2)
list1.insert(3)

console.log(list1);
