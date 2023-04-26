function solution(targets) {
  let ans = 1;
  targets.sort((a, b) => {
    if (a[1] === b[1]) return a[0] - b[0];
    return a[1] - b[1];
  });
  let en = targets[0][1];
  for (let i = 1; i < targets.length; i++) {
    const [s, e] = targets[i];
    if (s >= en) {
      en = e;
      ans++;
    }
  }
  return ans;
}
