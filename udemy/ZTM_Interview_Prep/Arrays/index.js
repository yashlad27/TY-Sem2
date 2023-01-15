const strings = ['a', 'b', 'c', 'd'];
console.log(strings);

console.log(strings[2])

strings.push('e'); // O(1)
console.log(strings);

strings.pop();
strings.pop(); // O(1)

// unshift:
strings.unshift('x'); // o(n)

// splice: add element in the middle
strings.splice(2, 0, 'alien')

console.log(strings);