
/***
 * Class to create a LinkedList Node
 * {
 *   this.val
 *   this.next
 * }
 */
function LinkedListNode(val) {
    this.val = val;
    this.next = null;
}

function LinkedList() {
  var head = null;
  var tail = null;
  function getValueAt(index) {
    index = index || 0;
    let point =  head;
    let i = 0;
    while (i <= index) {
      if(point === null) throw new Error("Index out of range");
      if (i === index) return point.val;
      i++; 
      point = point.next;
    }
    throw new Error("Index out of range");
  }
  function addAtEnd(val) {
    const node = new LinkedListNode(val);
    if(tail === null) {
      head = node;
      tail = node;
    } else {
      tail.next = node;
      tail = node;
    }
  }
  function getHead() {
    return head;
  }
  return {
    getValueAt,
    addAtEnd,
    getHead
  }
}