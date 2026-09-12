#!/usr/bin/env node
// Test logika kalkulator pajak HTML terhadap kasus latihan Mediawan (PP 20/2026).
// Usage: node test_kalkulator_pajak.js <kalkulator.html>
// Prinsip: ekstrak <script>, buang panggilan DOM, export const via globalThis, jalankan di vm sandbox.
const fs = require('fs');
const vm = require('vm');

const file = process.argv[2] || 'kalkulator.html';
let js = fs.readFileSync(file, 'utf8').match(/<script>([\s\S]*)<\/script>/)[1];
js = js.replace(/initApp\(\);/, '');
js += ';globalThis.__state = state; globalThis.__calcAll = calcAll;';

const fakeEl = { className:'', textContent:'', innerHTML:'', value:'', setAttribute(){}, addEventListener(){}, appendChild(){}, focus(){}, style:{} };
const sandbox = {
  document: { getElementById: () => fakeEl, createElement: () => ({ className:'', setAttribute(){}, addEventListener(){}, appendChild(){}, style:{} }), activeElement: null },
  window: null, console, Date, Math, Number, String, Object, Array, RegExp, parseInt, parseFloat, isNaN, Infinity, JSON,
};
sandbox.window = sandbox;
vm.createContext(sandbox);
try { vm.runInContext(js, sandbox); } catch (e) { console.log('EVAL NOTE (DOM):', e.message.slice(0, 80)); }

const state = sandbox.__state, calcAll = sandbox.__calcAll;
if (!state || !calcAll) { console.log('FATAL: state/calcAll tidak terdefinisi. Cek nama fungsi (mungkin calcAll beda).'); process.exit(1); }

function reset() {
  Object.assign(state, {
    omzet: 600000000, npm: 20, labaRp: 120000000, labaMode: 'pct', ptkp: 'K/2', subjek: 'op',
    klu: '47191', kota: 'kota2', kotaNama: 'Yogyakarta', normaManual: null, normaManualRaw: '',
    pekerjaanBebas: false, ahliKhusus: false, jasaPekerjaanBebas: false,
    omzetPasangan: 0, omzetPTLain: 0, tglTerdaftar: '',
  });
}
function t(nama, setup, ekspektasi) {
  reset(); Object.assign(state, setup);
  const r = calcAll();
  const canUse = r.final.canUse;
  const ok = canUse === ekspektasi;
  console.log(`${ok ? 'PASS' : 'FAIL'} | ${nama}: canUse=${canUse} (ekspektasi ${ekspektasi}) pajak=${r.final.pajak ? r.final.pajak.toLocaleString('id-ID') : '-'}`);
  if (!ok && r.masaTransisiInfo) console.log(`     info: ${r.masaTransisiInfo.slice(0, 130)}`);
  return ok;
}

let pass = 0, fail = 0;
// 7 kasus latihan Mediawan (kelas 02): benar = ekspektasi
pass += t('A. Bu Rina (OP warung, 2,4M)',       { subjek:'op', omzet:2400000000 }, true);
pass += t('B. PT Sinar Abadi (PT, 3,1M, 2025-03)', { subjek:'pt', omzet:3100000000, tglTerdaftar:'2025-03' }, true);
pass += t('C. Pak Doni (PT Perorangan 2M+istri 3,2M)', { subjek:'perorangan', omzet:2000000000, omzetPTLain:3200000000 }, false);
pass += t('D. drg. Sari (OP dokter gigi, 1,8M, profesi)', { subjek:'op', omzet:1800000000, pekerjaanBebas:true }, false);
pass += t('E. CV Berkah Jaya (CV, 4,2M, 2026-01)', { subjek:'cv', omzet:4200000000, tglTerdaftar:'2026-01' }, true);
pass += t('F. PT Digital Kreatif (konsultan IT, ahli khusus)', { subjek:'perorangan', omzet:2600000000, ahliKhusus:true, jasaPekerjaanBebas:true }, false);
pass += t('G. OP warung 2,4M (bukan profesi)',   { subjek:'op', omzet:2400000000, pekerjaanBebas:false }, true);

console.log(`\nHasil: ${pass} PASS / ${fail} FAIL`);
process.exit(fail > 0 ? 1 : 0);
