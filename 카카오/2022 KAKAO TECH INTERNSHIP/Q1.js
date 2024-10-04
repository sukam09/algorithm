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
/*
+가 ||보다 연산자 우선순위가 높음에 주의
예를 들어, map에서 가져오는 코드를 아래와 같이 짜면 오답
map.get(sv[0]) || 0 + (4 - c)
*/