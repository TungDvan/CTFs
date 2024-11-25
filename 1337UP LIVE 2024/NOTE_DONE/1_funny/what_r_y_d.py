import re

# Chuỗi chứa dữ liệu
data = """
 30:        2254 LOAD_NAME            (o)
            2256 POP_TOP
            2258 LOAD_NAME            (f)
            2260 POP_TOP
            2262 LOAD_NAME            (y)
            2264 POP_TOP
            2266 LOAD_NAME            (n)
            2268 POP_TOP
            2270 LOAD_NAME            (g)
            2272 POP_TOP
            2274 LOAD_NAME            (r)
            2276 POP_TOP
            2278 LOAD_NAME            (b)
            2280 POP_TOP
            2282 LOAD_NAME            (k)
            2284 POP_TOP
            2286 LOAD_NAME            (a)
            2288 POP_TOP
            2290 LOAD_NAME            (l)
            2292 POP_TOP
            2294 LOAD_NAME            (d)
            2296 POP_TOP
            2298 LOAD_NAME            (j)
            2300 POP_TOP
            2302 LOAD_NAME            (x)
            2304 POP_TOP
            2306 LOAD_NAME            (z)
            2308 POP_TOP
            2310 LOAD_NAME            (n)
            2312 POP_TOP
            2314 LOAD_NAME            (v)
            2316 POP_TOP
            2318 LOAD_NAME            (v)
            2320 POP_TOP
            2322 LOAD_NAME            (i)
            2324 POP_TOP
            2326 LOAD_NAME            (j)
            2328 POP_TOP
            2330 LOAD_NAME            (k)
            2332 POP_TOP
            2334 LOAD_NAME            (p)
            2336 POP_TOP
            2338 LOAD_NAME            (e)
            2340 POP_TOP
            2342 LOAD_NAME            (c)
            2344 POP_TOP
            2346 LOAD_NAME            (f)
            2348 POP_TOP
            2350 LOAD_NAME            (g)
            2352 POP_TOP
            2354 LOAD_NAME            (d)
            2356 POP_TOP
            2358 LOAD_NAME            (b)
            2360 POP_TOP
            2362 LOAD_NAME            (w)
            2364 POP_TOP
            2366 LOAD_NAME            (r)
            2368 POP_TOP
            2370 LOAD_NAME            (k)
            2372 POP_TOP
            2374 LOAD_NAME            (m)
            2376 POP_TOP
            2378 LOAD_NAME            (g)
            2380 POP_TOP
            2382 LOAD_NAME            (j)
            2384 POP_TOP
            2386 LOAD_NAME            (i)
            2388 POP_TOP
            2390 LOAD_NAME            (n)
            2392 POP_TOP
            2394 LOAD_NAME            (s)
            2396 POP_TOP
            2398 LOAD_NAME            (l)
            2400 POP_TOP
            2402 LOAD_NAME            (u)
            2404 POP_TOP
            2406 LOAD_NAME            (a)
            2408 POP_TOP
            2410 LOAD_NAME            (h)
            2412 POP_TOP
            2414 LOAD_NAME            (z)
            2416 POP_TOP
            2418 LOAD_NAME            (y)
            2420 POP_TOP
            2422 LOAD_NAME            (f)
            2424 POP_TOP
            2426 LOAD_NAME            (c)
            2428 POP_TOP
            2430 LOAD_NAME            (k)
            2432 POP_TOP
            2434 LOAD_NAME            (y)
            2436 POP_TOP
            2438 LOAD_NAME            (k)
            2440 POP_TOP
            2442 LOAD_NAME            (g)
            2444 POP_TOP
            2446 LOAD_NAME            (k)
            2448 POP_TOP
            2450 LOAD_NAME            (w)
            2452 POP_TOP
            2454 LOAD_NAME            (l)
            2456 POP_TOP
            2458 LOAD_NAME            (m)
            2460 POP_TOP
            2462 LOAD_NAME            (r)
            2464 POP_TOP
            2466 LOAD_NAME            (h)
            2468 POP_TOP
            2470 LOAD_NAME            (r)
            2472 POP_TOP
            2474 LOAD_NAME            (u)
            2476 POP_TOP
            2478 LOAD_NAME            (b)
            2480 POP_TOP
            2482 LOAD_NAME            (j)
            2484 POP_TOP
            2486 LOAD_NAME            (y)
            2488 POP_TOP
            2490 LOAD_NAME            (f)
            2492 POP_TOP
            2494 LOAD_NAME            (m)
            2496 POP_TOP
            2498 LOAD_NAME            (f)
            2500 POP_TOP
            2502 LOAD_NAME            (t)
            2504 POP_TOP
            2506 LOAD_NAME            (l)
            2508 POP_TOP
            2510 LOAD_NAME            (a)
            2512 POP_TOP
            2514 LOAD_NAME            (f)
            2516 POP_TOP
            2518 LOAD_NAME            (u)
            2520 POP_TOP
            2522 LOAD_NAME            (j)
            2524 POP_TOP
            2526 LOAD_NAME            (m)
            2528 POP_TOP
            2530 LOAD_NAME            (b)
            2532 POP_TOP
            2534 LOAD_NAME            (i)
            2536 POP_TOP
            2538 LOAD_NAME            (j)
            2540 POP_TOP
            2542 LOAD_NAME            (v)
            2544 POP_TOP
            2546 LOAD_NAME            (w)
            2548 POP_TOP
            2550 LOAD_NAME            (o)
            2552 POP_TOP
            2554 LOAD_NAME            (l)
            2556 POP_TOP
            2558 LOAD_NAME            (w)
            2560 POP_TOP
            2562 LOAD_NAME            (p)
            2564 POP_TOP
            2566 LOAD_NAME            (u)
            2568 POP_TOP
            2570 LOAD_NAME            (a)
            2572 POP_TOP
            2574 LOAD_NAME            (y)
            2576 POP_TOP
            2578 LOAD_NAME            (y)
            2580 POP_TOP
            2582 LOAD_NAME            (x)
            2584 POP_TOP
            2586 LOAD_NAME            (y)
            2588 POP_TOP
            2590 LOAD_NAME            (b)
            2592 POP_TOP
            2594 LOAD_NAME            (d)
            2596 POP_TOP
            2598 LOAD_NAME            (o)
            2600 POP_TOP
            2602 LOAD_NAME            (l)
            2604 POP_TOP
            2606 LOAD_NAME            (m)
            2608 POP_TOP
            2610 LOAD_NAME            (f)
            2612 POP_TOP
            2614 LOAD_NAME            (q)
            2616 POP_TOP
            2618 LOAD_NAME            (u)
            2620 POP_TOP
            2622 LOAD_NAME            (l)
            2624 POP_TOP
            2626 LOAD_NAME            (d)
            2628 POP_TOP
            2630 LOAD_NAME            (x)
            2632 POP_TOP
            2634 LOAD_NAME            (f)
            2636 POP_TOP
            2638 LOAD_NAME            (m)
            2640 POP_TOP
            2642 LOAD_NAME            (v)
            2644 POP_TOP
            2646 LOAD_NAME            (x)
            2648 POP_TOP
            2650 LOAD_NAME            (b)
            2652 POP_TOP
            2654 LOAD_NAME            (z)
            2656 POP_TOP
            2658 LOAD_NAME            (l)
            2660 POP_TOP
            2662 LOAD_NAME            (i)
            2664 POP_TOP
            2666 LOAD_NAME            (w)
            2668 POP_TOP
            2670 LOAD_NAME            (i)
            2672 POP_TOP
            2674 LOAD_NAME            (x)
            2676 POP_TOP
            2678 LOAD_NAME            (e)
            2680 POP_TOP
            2682 LOAD_NAME            (s)
            2684 POP_TOP
            2686 LOAD_NAME            (p)
            2688 POP_TOP
            2690 LOAD_NAME            (n)
            2692 POP_TOP
            2694 LOAD_NAME            (z)
            2696 POP_TOP
            2698 LOAD_NAME            (a)
            2700 POP_TOP
            2702 LOAD_NAME            (x)
            2704 POP_TOP
            2706 LOAD_NAME            (j)
            2708 POP_TOP
            2710 LOAD_NAME            (y)
            2712 POP_TOP
            2714 LOAD_NAME            (r)
            2716 POP_TOP
            2718 LOAD_NAME            (m)
            2720 POP_TOP
            2722 LOAD_NAME            (r)
            2724 POP_TOP
            2726 LOAD_NAME            (h)
            2728 POP_TOP
            2730 LOAD_NAME            (f)
            2732 POP_TOP
            2734 LOAD_NAME            (h)
            2736 POP_TOP
            2738 LOAD_NAME            (o)
            2740 POP_TOP
            2742 LOAD_NAME            (z)
            2744 POP_TOP
            2746 LOAD_NAME            (i)
            2748 POP_TOP
            2750 LOAD_NAME            (z)
            2752 POP_TOP
            2754 LOAD_NAME            (g)
            2756 POP_TOP
            2758 LOAD_NAME            (f)
            2760 POP_TOP
            2762 LOAD_NAME            (v)
            2764 POP_TOP
            2766 LOAD_NAME            (a)
            2768 POP_TOP
            2770 LOAD_NAME            (n)
            2772 POP_TOP
"""

# Sử dụng biểu thức chính quy để tìm các ký tự trong ngoặc đơn
result = re.findall(r'\((\w)\)', data)

# Ghép các ký tự thành chuỗi
output = ''.join(result)

print(output)  # Kết quả: brybefej

