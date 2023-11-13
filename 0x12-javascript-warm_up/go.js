#!/usr/bin/node
/* myVar = 89;
require('./100-let_me_const');
console.log(myVar);
*/

/* const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
}); */

const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;

addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
