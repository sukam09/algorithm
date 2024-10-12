function solution(today, terms, privacies) {
  const conv = s => {
    const [y, m, d] = s.split('.').map(v => +v);
    return y * 28 * 12 + m * 28 + d;
  }
  
  const map = new Map();
  for (const term of terms) {
    const [type, duration] = term.split(' ');
    map.set(type, 28 * +duration);
  }
  
  const td = conv(today);
  let idx = 1;
  const ans = [];
  
  for (const privacy of privacies) {
    const [date, type] = privacy.split(' ');
    const dd = conv(date);
    if (dd + map.get(type) <= td) {
      ans.push(idx);
    }
    idx++;
  }
  
  return ans;
}
