function incrementAndCall(number, theFunction) {
  number += 1;
  theFunction(number);
}

// Example usage:
incrementAndCall(4, function (nb) {
  console.log('New value: ' + nb);
});
