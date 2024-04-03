
lodash = require('lodash');
//array

arr = [4, 2, 3, 1, 5];

// sort array ,filter array and find maximum
sorted_arr = lodash.sortBy(arr);

//filter
myArr = [
    { name: "john", age: 23 },
    { name: "john", age: 43 },
    { name: "jim", age: 101 },
    { name: "bob", age: 67 }
  ];
  
filteredByName = lodash.filter(myArr, function(o) {
    return o.name === 'john';});
//returns an array of objects where the name is john

maxx = lodash.max(arr)

console.log('Sorted Array:', sorted_arr);
console.log('Maximum number in array:', maxx);
console.log('Filtered array: ', filteredByName)

