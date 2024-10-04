function solution(alp, cop, problems) {
  const MX = 99999;
  const dp = [...Array(155)].map(() => Array(155).fill(MX)); // 배열 크기를 155보다 작게 하면 틀림 why?
  
  let alp_max = -1;
  let cop_max = -1;
  for (const [a, b] of problems) {
    alp_max = Math.max(alp_max, a);
    cop_max = Math.max(cop_max, b);
  }
  
  // alp, cop가 alp_max, cop_max보다 클 때 예외처리 필요
  alp = Math.min(alp, alp_max);
  cop = Math.min(cop, cop_max);
  
  dp[alp][cop] = 0;
  
  for (let i = alp; i <= alp_max; i++) {
    for (let j = cop; j <= cop_max; j++) {
      dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
      dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);
      for (const [a, b, c, d, e] of problems) {
        if (i < a || j < b) {
          continue;
        }
        const alp_nxt = Math.min(alp_max, i + c);
        const cop_nxt = Math.min(cop_max, j + d);
        dp[alp_nxt][cop_nxt] = Math.min(dp[alp_nxt][cop_nxt], dp[i][j] + e);
      }
    }
  }
  
  return dp[alp_max][cop_max];
}
