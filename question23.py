let car: string = 'subaru';

// Test 1
console.log("Is car == 'subaru'? I predict True.");
console.log(car == 'subaru');

// Test 2
console.log("Is car != 'toyota'? I predict True.");
console.log(car != 'toyota');

// Test 3
console.log("Is car === 'Subaru'? I predict False.");
console.log(car === 'Subaru');

// Test 4
console.log("Is car !== 'Subaru'? I predict True.");
console.log(car !== 'Subaru');

// Test 5
let isJapaneseCar: boolean = true;
console.log("Is car == 'subaru' and isJapaneseCar is True? I predict True.");
console.log(car == 'subaru' && isJapaneseCar);

// Test 6
let hasSunroof: boolean = false;
console.log("Is car == 'subaru' or hasSunroof is True? I predict True.");
console.log(car == 'subaru' || hasSunroof);

// Test 7
let isSedan: boolean = true;
console.log("Is car == 'subaru' and isSedan is False? I predict False.");
console.log(car == 'subaru' && !isSedan);

// Test 8
let isConvertible: boolean = false;
console.log("Is car != 'subaru' or isConvertible is False? I predict False.");
console.log(car != 'subaru' || !isConvertible);

// Test 9
let isLuxuryCar: boolean = false;
console.log("Is car == 'subaru' or isLuxuryCar is True? I predict True.");
console.log(car == 'subaru' || isLuxuryCar);

// Test 10
let isCompactCar: boolean = true;
console.log("Is car != 'subaru' and isCompactCar is False? I predict False.");
console.log(car != 'subaru' && !isCompactCar);
