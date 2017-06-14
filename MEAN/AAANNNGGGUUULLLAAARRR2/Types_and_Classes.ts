var myNum: number = 5;

var myString: string = 'Hello Universe';

var myArr: Array<number> = [1, 2, 3, 4];

var myObj: object = { name: 'Bill' };

var anythingVariable: any = 'Hey';

var anythingVariable: any = 25;

var arrayOne: Array<boolean> = [true, false, true, true];

var arrayTwo: (number|string|boolean|number)[] = [1, 'abc', true, 2];

var myObj: object = { x: 5, y: 10 };

class MyNode {
    val: number;
    constructor(val: number) {
        this.val = 0;
        this.val = val
    }
    doSomethingFun() {
      var _priv: number;
      this._priv = 10;
    }
}
let firstSLNode = new MyNode(1);

function myFunction(): void {
    console.log("Hello World");
    return;

function sendingErrors(): never{
	throw new Error('Error message')
