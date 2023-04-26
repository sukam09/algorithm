const conv = (h, m) => h * 60 + m;

function solution(plans) {
  const ans = [];
  const n = plans.length;
  for (let i = 0; i < n; i++) {
    const [h, m] = plans[i][1].split(':').map(Number);
    plans[i][1] = conv(h, m);
    plans[i][2] = +plans[i][2];
  }
  plans.sort((a, b) => a[1] - b[1]);
  let time = 0;
  // 과제가 끝나는 시간은 24:00을 아득히 넘을 수 있음
  const en = conv(24, 0) + 100000;
  let idx = 0;
  const stk = [];
  while (time < en) {
    if (stk.length && stk[stk.length - 1][1] === 0) {
      ans.push(stk.pop()[0]);
    }
    if (idx < n && time === plans[idx][1]) {
      stk.push([plans[idx][0], plans[idx][2]]);
      idx++;
    }
    time++;
    if (stk.length) stk[stk.length - 1][1]--;
  }
  return ans;
}
