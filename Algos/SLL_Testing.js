function Node(value) {
    this.val = value;
    this.next = null;
    }

function SLL() {
    this.head = null;

    this.remove_neg = function(val) {
        if(!this.head) {
            return this.head;
        }
    }
    var current = this.head.next //allows us to TRAVERSE through list (NOT ITERATE)
    var previous = this.head
    while(previous.val < 0) {
      this.head = current;
      return this.head;
    }
    while(current) {
        if(previous.val < 0) {
            this.head = current
        }
    }
}

var list1 = new SLL()

list1.insert(4)
list1.insert(3)
list1.insert(-1)
list1.insert(2)

console.log("original list 1", list1.head)
console.log("return of split on value method", list1.splitOnVal(list2, 4))
console.log("split on list 1", list1.head)
