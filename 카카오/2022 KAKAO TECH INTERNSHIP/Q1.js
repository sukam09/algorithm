function solution(survey, choices) {
  const map = new Map();
  const n = survey.length;
  const mbtis = ['RT', 'CF', 'JM', 'AN'];
  for (let i = 0; i < n; i++) {
    const sv = survey[i];
    const c = choices[i];
    
    if (c <= 3) {
      map.set(sv[0], (map.get(sv[0]) || 0) + (4 - c));
    } else if (c >= 5) {
      map.set(sv[1], (map.get(sv[1]) || 0) + (c - 4));
    }
  }
  let ans = '';
  for (const x of mbtis) {
    const a = map.get(x[0]) || 0;
    const b = map.get(x[1]) || 0;
    if (a >= b) {
      ans += x[0];
    } else {
      ans += x[1];
    }
  }
  return ans;
}
