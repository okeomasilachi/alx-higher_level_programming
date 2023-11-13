#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  const num = args[0];
  for (let i = 0; i < args.length; i++) {
    if (args[i] < num) {
      console.log(args[i]);
      break;
    }
  }
}
