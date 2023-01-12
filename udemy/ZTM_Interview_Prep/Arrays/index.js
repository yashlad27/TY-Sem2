const strings = ['a', 'b', 'c', 'd'];
console.log(strings);

strings.push('e'); // O(1)
console.log(strings);

strings.pop();
strings.pop(); // O(1)

console.log(strings);