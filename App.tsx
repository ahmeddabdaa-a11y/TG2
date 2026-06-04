/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';
import { CheckCircle, Terminal, Shield } from 'lucide-react';

export default function App() {
  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-100 font-sans p-4 sm:p-8 flex flex-col items-center justify-center">
      <div className="max-w-3xl w-full bg-neutral-900 border border-neutral-800 rounded-2xl p-6 sm:p-10 shadow-2xl">
        <div className="flex flex-col-reverse sm:flex-row items-center sm:justify-between mb-8 gap-4">
          <div className="flex items-center space-x-3">
            <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-white font-mono">TG Star Sniper - Phase 1</h1>
            <Shield className="w-8 h-8 text-emerald-500 hidden sm:block" />
          </div>
          <div className="px-4 py-1.5 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 rounded-full text-sm font-semibold">
            Status: Stealth Ready
          </div>
        </div>
        
        <div className="bg-neutral-800/50 border border-neutral-700/50 rounded-xl p-6 mb-8 text-right" dir="rtl">
          <div className="flex items-center space-x-3 space-x-reverse mb-5">
            <CheckCircle className="w-7 h-7 text-emerald-500" />
            <h2 className="text-2xl font-bold text-emerald-400">تم إنشاء المرحلة الأولى بنجاح!</h2>
          </div>
          <p className="text-neutral-300 leading-relaxed text-lg pb-4">
            تم بناء هيكل النظام الأساسي (Phase 1) بدقة حسب متطلباتك كـ Enterprise-grade، ويشمل:
          </p>
          <ul className="list-disc list-inside text-neutral-400 space-y-3 text-base sm:text-lg pr-4 font-medium marker:text-blue-500">
            <li>هيكل المشروع الكامل والمنظم (Architecture Setup).</li>
            <li>نظام القوائم التفاعلية CLI باللغة العربية باستخدام (Rich + Typer).</li>
            <li>إدارة الحسابات الشاملة، بروكسي، وحفظ الجلسات (Account Management).</li>
            <li>نظام التشفير (Fernet Encryption) لحماية الـ Sessions والمفاتيح بدلاً من Plain text.</li>
            <li>إعدادات Docker Compose و المتطلبات (Requirements).</li>
          </ul>
        </div>

        <div className="flex items-center justify-between p-5 bg-[#0a0a0a] border border-neutral-800 rounded-lg">
          <div className="flex items-center space-x-4 space-x-reverse mx-auto text-blue-400">
            <Terminal className="w-5 h-5 flex-shrink-0" />
            <span className="font-mono text-sm sm:text-base break-all">python tg-star-sniper-sustainable/main.py</span>
          </div>
        </div>

        <p className="mt-8 text-sm sm:text-base text-neutral-500 text-center">
          لتحميل المشروع بالكامل: اضغط على أيقونة الإعدادات (Settings) في أعلى الشاشة واختر <strong className="text-white">Export to ZIP</strong>.
          <br/>
          بعد ذلك يمكنك رفعه إلى السيرفر (VPS) أو الاستضافة عبر FileZilla أو MobaXterm، ثم فك الضغط وتشغيل <code className="text-blue-400">docker-compose up -d --build</code> أو <code className="text-blue-400">python main.py</code>.
        </p>
      </div>
    </div>
  );
}
