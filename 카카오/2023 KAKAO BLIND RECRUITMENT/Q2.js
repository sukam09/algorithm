function solution(cap, n, deliveries, pickups) {
  let ans = 0;
  let ds = 0;
  let ps = 0;
  for (let i = n - 1; i >= 0; i--) {
    ds += deliveries[i];
    ps += pickups[i];
    while (ds > 0 || ps > 0) {
      ds -= cap;
      ps -= cap;
      ans += (i + 1) * 2;
    }
  }
  return ans;
}
/*
ds, ps가 음수인 경우는 다음에 갈 위치까지 이미 배달, 수거를 처리했다고 생각하면 됨
즉, 미리 쟁여둔다고 봐도 될듯
*/
