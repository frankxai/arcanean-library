"use client";

import { useEffect, useRef } from "react";
import Link from "next/link";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  const headingRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    if (error?.digest) {
      console.error(error.digest);
    }
  }, [error]);

  useEffect(() => {
    headingRef.current?.focus();
  }, []);

  return (
    <main className="mx-auto flex min-h-[60vh] max-w-4xl flex-col items-center justify-center p-6 text-center">
      <div className="relative overflow-hidden rounded-3xl border border-[#2a385c]/60 bg-gradient-to-br from-[#0f1627] via-[#0b1220] to-[#060b16] p-10 shadow-[0_0_120px_rgba(120,166,255,0.18)]">
        <div className="pointer-events-none absolute inset-0 opacity-40" aria-hidden="true">
          <div className="absolute -left-24 top-16 h-72 w-72 rounded-full bg-[#76a6ff]/30 blur-3xl" />
          <div className="absolute right-[-10%] top-1/3 h-80 w-80 rounded-full bg-[#7fffd4]/25 blur-3xl" />
        </div>
        <div className="relative space-y-6">
          <div className="flex items-center justify-center gap-3 text-xs uppercase tracking-[0.4em] text-[#9bb1d0]">
            <span>Arcanea Library</span>
            <span className="h-px w-12 bg-[#23335a]" aria-hidden="true" />
            <span>Notice</span>
          </div>
          <h1
            ref={headingRef}
            tabIndex={-1}
            className="text-3xl font-semibold tracking-tight text-white focus:outline-none md:text-5xl"
          >
            Something quieted the stacks
          </h1>
          <p className="mx-auto max-w-lg text-base text-[#c7d6f1]">
            An unexpected whisper paused this part of the library. You can try refreshing this section or return home.
          </p>
          <div className="flex flex-wrap justify-center gap-4 pt-4">
            <button
              type="button"
              onClick={reset}
              className="rounded-full bg-[#78a6ff] px-6 py-3 text-sm font-semibold text-black transition hover:bg-[#7fffd4] focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-[#05070d] focus-visible:ring-[#7fffd4]"
            >
              Try again
            </button>
            <Link
              href="/"
              className="rounded-full border border-[#78a6ff]/40 px-6 py-3 text-sm font-semibold text-[#c7d6f1] transition hover:border-[#7fffd4] hover:text-[#7fffd4] focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-[#05070d] focus-visible:ring-[#7fffd4]"
            >
              Return home
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
}
