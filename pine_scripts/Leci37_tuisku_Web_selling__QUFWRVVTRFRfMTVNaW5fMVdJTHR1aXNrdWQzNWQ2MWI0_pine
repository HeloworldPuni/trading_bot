//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Williams_Vix_Fix
// ID_model: AAVEUSDT_15Min_1WIL_d35d61b4 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AAVEUSDT_15Min_1WIL_d35d61b4", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AAVEUSDT_15Min_d35d61b4(rangeHigh, rangeLow, midLine, sDev, lowerBand, wvf, Color_con1, colInt, Color_con2, upperBand)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( wvf <= 2.38872 )
		if( Color_con2 <= -5.91774 )
			if( midLine <= 0.946785 )
				if( Color_con1 <= -0.541146 )
					if( Color_con1 <= -1.64593 )
						ret := 0.000000
					if( Color_con1 > -1.64593 )
						if( Color_con2 <= -7.66475 )
							ret := 1.000000 // buy
						if( Color_con2 > -7.66475 )
							if( upperBand <= 1.58557 )
								ret := 0.500000
							if( upperBand > 1.58557 )
								if( Color_con2 <= -6.03692 )
									ret := 0.750000 // buy
								if( Color_con2 > -6.03692 )
									ret := 1.000000 // buy
				if( Color_con1 > -0.541146 )
					if( Color_con1 <= -0.453173 )
						ret := -0.428571
					if( Color_con1 > -0.453173 )
						if( wvf <= 0.989815 )
							if( midLine <= 0.712821 )
								ret := 0.166667
							if( midLine > 0.712821 )
								ret := -0.250000
						if( wvf > 0.989815 )
							ret := 0.500000
			if( midLine > 0.946785 )
				if( Color_con2 <= -8.52423 )
					if( upperBand <= 3.3953 )
						if( wvf <= 1.54136 )
							if( midLine <= 1.46596 )
								if( Color_con2 <= -10.3679 )
									ret := -0.945946 // sell
								if( Color_con2 > -10.3679 )
									ret := -0.700000 // sell
							if( midLine > 1.46596 )
								if( midLine <= 1.6125 )
									ret := 0.000000
								if( midLine > 1.6125 )
									ret := -0.736842 // sell
						if( wvf > 1.54136 )
							if( upperBand <= 2.21721 )
								if( upperBand <= 2.10616 )
									ret := -0.500000
								if( upperBand > 2.10616 )
									ret := -1.000000 // sell
							if( upperBand > 2.21721 )
								if( Color_con2 <= -9.60013 )
									ret := 0.880000 // buy
								if( Color_con2 > -9.60013 )
									ret := -0.500000
					if( upperBand > 3.3953 )
						if( upperBand <= 16.7138 )
							if( wvf <= 2.32857 )
								if( lowerBand <= -3.57382 )
									ret := -0.600000
								if( lowerBand > -3.57382 )
									ret := 0.402367
							if( wvf > 2.32857 )
								ret := -1.000000 // sell
						if( upperBand > 16.7138 )
							if( midLine <= 10.7233 )
								if( lowerBand <= 1.56697 )
									ret := -0.720930 // sell
								if( lowerBand > 1.56697 )
									ret := 0.400000
							if( midLine > 10.7233 )
								if( Color_con2 <= -11.9944 )
									ret := 1.000000 // buy
								if( Color_con2 > -11.9944 )
									ret := 0.750000 // buy
				if( Color_con2 > -8.52423 )
					if( midLine <= 4.78275 )
						if( sDev <= 1.22753 )
							if( upperBand <= 3.07294 )
								if( sDev <= 0.68714 )
									ret := -0.095238
								if( sDev > 0.68714 )
									ret := -0.700000 // sell
							if( upperBand > 3.07294 )
								if( sDev <= 1.09265 )
									ret := 0.000000
								if( sDev > 1.09265 )
									ret := 0.333333
						if( sDev > 1.22753 )
							if( wvf <= 1.01595 )
								if( Color_con2 <= -6.02799 )
									ret := -0.154964
								if( Color_con2 > -6.02799 )
									ret := -0.679245
							if( wvf > 1.01595 )
								if( midLine <= 1.53537 )
									ret := 0.723404 // buy
								if( midLine > 1.53537 )
									ret := -0.019956
					if( midLine > 4.78275 )
						if( lowerBand <= -1.00838 )
							if( sDev <= 7.27577 )
								if( upperBand <= 11.8096 )
									ret := -0.583333
								if( upperBand > 11.8096 )
									ret := 0.650000
							if( sDev > 7.27577 )
								if( midLine <= 5.95351 )
									ret := -1.000000 // sell
								if( midLine > 5.95351 )
									ret := -0.200000
						if( lowerBand > -1.00838 )
							if( sDev <= 5.22646 )
								if( midLine <= 5.83984 )
									ret := -0.646154
								if( midLine > 5.83984 )
									ret := -0.156250
							if( sDev > 5.22646 )
								if( Color_con2 <= -6.06677 )
									ret := -0.759124 // sell
								if( Color_con2 > -6.06677 )
									ret := 0.125000
		if( Color_con2 > -5.91774 )
			if( sDev <= 1.72201 )
				if( sDev <= 1.31194 )
					if( Color_con2 <= -5.09219 )
						if( wvf <= 0.83152 )
							if( lowerBand <= 0.136875 )
								if( midLine <= 0.955125 )
									ret := 0.090909
								if( midLine > 0.955125 )
									ret := -0.750000 // sell
							if( lowerBand > 0.136875 )
								if( lowerBand <= 0.434175 )
									ret := 0.801653 // buy
								if( lowerBand > 0.434175 )
									ret := -0.428571
						if( wvf > 0.83152 )
							if( upperBand <= 2.55114 )
								if( sDev <= 0.695169 )
									ret := 0.380952
								if( sDev > 0.695169 )
									ret := -0.380952
							if( upperBand > 2.55114 )
								if( sDev <= 1.27874 )
									ret := 0.511111
								if( sDev > 1.27874 )
									ret := -0.400000
					if( Color_con2 > -5.09219 )
						if( Color_con2 <= -1.71548 )
							if( lowerBand <= 0.205433 )
								if( midLine <= 1.17456 )
									ret := 0.004977
								if( midLine > 1.17456 )
									ret := 0.296763
							if( lowerBand > 0.205433 )
								if( upperBand <= 1.49377 )
									ret := 0.171123
								if( upperBand > 1.49377 )
									ret := -0.128041
						if( Color_con2 > -1.71548 )
							if( Color_con1 <= -1.35079 )
								if( wvf <= 0.472786 )
									ret := 0.021024
								if( wvf > 0.472786 )
									ret := 0.128856
							if( Color_con1 > -1.35079 )
								if( Color_con2 <= -1.2423 )
									ret := 0.102445
								if( Color_con2 > -1.2423 )
									ret := 0.031369
				if( sDev > 1.31194 )
					if( upperBand <= 4.40597 )
						if( wvf <= 0.43365 )
							if( midLine <= 2.15556 )
								if( Color_con2 <= -3.36352 )
									ret := -0.494253
								if( Color_con2 > -3.36352 )
									ret := 0.157472
							if( midLine > 2.15556 )
								if( wvf <= 0.271666 )
									ret := 0.900000 // buy
								if( wvf > 0.271666 )
									ret := 0.500000
						if( wvf > 0.43365 )
							if( midLine <= 2.5018 )
								if( midLine <= 0.898393 )
									ret := 0.214286
								if( midLine > 0.898393 )
									ret := -0.093742
							if( midLine > 2.5018 )
								if( Color_con1 <= -2.29635 )
									ret := -0.003623
								if( Color_con1 > -2.29635 )
									ret := 0.487342
					if( upperBand > 4.40597 )
						if( Color_con2 <= -1.72257 )
							if( Color_con1 <= -2.78643 )
								if( sDev <= 1.52364 )
									ret := -0.536232
								if( sDev > 1.52364 )
									ret := -0.086957
							if( Color_con1 > -2.78643 )
								if( lowerBand <= 1.95396 )
									ret := 0.607143
								if( lowerBand > 1.95396 )
									ret := -1.000000 // sell
						if( Color_con2 > -1.72257 )
							if( wvf <= 2.19645 )
								if( Color_con1 <= -2.49283 )
									ret := -0.472727
								if( Color_con1 > -2.49283 )
									ret := -0.918919 // sell
							if( wvf > 2.19645 )
								if( Color_con1 <= -2.42213 )
									ret := 0.086957
								if( Color_con1 > -2.42213 )
									ret := -0.500000
			if( sDev > 1.72201 )
				if( Color_con1 <= -5.22599 )
					if( sDev <= 4.71503 )
						if( Color_con2 <= -5.0989 )
							if( midLine <= 3.06706 )
								if( sDev <= 3.61034 )
									ret := 0.857143 // buy
								if( sDev > 3.61034 )
									ret := -0.047619
							if( midLine > 3.06706 )
								if( upperBand <= 8.67143 )
									ret := -0.674603
								if( upperBand > 8.67143 )
									ret := -0.202532
						if( Color_con2 > -5.0989 )
							if( Color_con2 <= -3.71224 )
								if( midLine <= 4.29388 )
									ret := -0.096012
								if( midLine > 4.29388 )
									ret := 0.143713
							if( Color_con2 > -3.71224 )
								if( Color_con2 <= -2.99106 )
									ret := -0.380952
								if( Color_con2 > -2.99106 )
									ret := 0.135593
					if( sDev > 4.71503 )
						if( midLine <= 5.54531 )
							if( wvf <= 1.92615 )
								if( Color_con1 <= -7.94658 )
									ret := 0.495575
								if( Color_con1 > -7.94658 )
									ret := -0.080357
							if( wvf > 1.92615 )
								if( lowerBand <= -0.555307 )
									ret := 0.875000 // buy
								if( lowerBand > -0.555307 )
									ret := 0.000000
						if( midLine > 5.54531 )
							if( lowerBand <= 1.47159 )
								ret := -1.000000 // sell
							if( lowerBand > 1.47159 )
								ret := 0.000000
				if( Color_con1 > -5.22599 )
					if( midLine <= 2.04168 )
						if( sDev <= 2.07038 )
							if( upperBand <= 3.93932 )
								if( Color_con1 <= -3.34402 )
									ret := 0.525862
								if( Color_con1 > -3.34402 )
									ret := 0.109919
							if( upperBand > 3.93932 )
								if( Color_con1 <= -3.0966 )
									ret := -0.491228
								if( Color_con1 > -3.0966 )
									ret := -0.032258
						if( sDev > 2.07038 )
							if( wvf <= 1.2482 )
								if( Color_con2 <= -1.03106 )
									ret := 0.032258
								if( Color_con2 > -1.03106 )
									ret := 0.666667
							if( wvf > 1.2482 )
								if( Color_con2 <= -4.08795 )
									ret := 0.500000
								if( Color_con2 > -4.08795 )
									ret := -0.213080
					if( midLine > 2.04168 )
						if( lowerBand <= -1.22918 )
							if( Color_con2 <= -2.12818 )
								if( Color_con2 <= -4.61429 )
									ret := 0.428571
								if( Color_con2 > -4.61429 )
									ret := 0.870370 // buy
							if( Color_con2 > -2.12818 )
								ret := -0.166667
						if( lowerBand > -1.22918 )
							if( upperBand <= 6.37775 )
								if( midLine <= 3.71191 )
									ret := 0.148400
								if( midLine > 3.71191 )
									ret := 0.423913
							if( upperBand > 6.37775 )
								if( Color_con1 <= -4.64381 )
									ret := 0.076596
								if( Color_con1 > -4.64381 )
									ret := -0.461538
	if( wvf > 2.38872 )
		if( midLine <= 3.43358 )
			if( Color_con2 <= 4.9195 )
				if( upperBand <= 7.01434 )
					if( sDev <= 1.6293 )
						if( midLine <= 3.00709 )
							if( midLine <= 1.90561 )
								if( Color_con1 <= 0.877046 )
									ret := 0.084304
								if( Color_con1 > 0.877046 )
									ret := 0.440000
							if( midLine > 1.90561 )
								if( sDev <= 1.47849 )
									ret := 0.156651
								if( sDev > 1.47849 )
									ret := 0.327645
						if( midLine > 3.00709 )
							if( Color_con1 <= -0.547476 )
								if( midLine <= 3.02075 )
									ret := -0.714286 // sell
								if( midLine > 3.02075 )
									ret := -0.119332
							if( Color_con1 > -0.547476 )
								if( lowerBand <= 2.30872 )
									ret := 0.711864 // buy
								if( lowerBand > 2.30872 )
									ret := -0.363636
					if( sDev > 1.6293 )
						if( Color_con2 <= -6.46075 )
							if( upperBand <= 6.02964 )
								if( upperBand <= 3.34514 )
									ret := 0.500000
								if( upperBand > 3.34514 )
									ret := -0.853659 // sell
							if( upperBand > 6.02964 )
								ret := 1.000000 // buy
						if( Color_con2 > -6.46075 )
							if( Color_con2 <= -1.12173 )
								if( Color_con1 <= -1.42054 )
									ret := 0.285181
								if( Color_con1 > -1.42054 )
									ret := 0.039422
							if( Color_con2 > -1.12173 )
								if( upperBand <= 3.53645 )
									ret := 0.118644
								if( upperBand > 3.53645 )
									ret := 0.016496
				if( upperBand > 7.01434 )
					if( Color_con1 <= -1.0694 )
						if( upperBand <= 8.80751 )
							if( Color_con1 <= -5.44843 )
								ret := 0.666667
							if( Color_con1 > -5.44843 )
								if( Color_con1 <= -1.32652 )
									ret := -0.391566
								if( Color_con1 > -1.32652 )
									ret := -0.862069 // sell
						if( upperBand > 8.80751 )
							if( midLine <= 2.93047 )
								ret := -0.250000
							if( midLine > 2.93047 )
								if( Color_con1 <= -3.27295 )
									ret := 0.727273 // buy
								if( Color_con1 > -3.27295 )
									ret := 0.000000
					if( Color_con1 > -1.0694 )
						if( sDev <= 4.7221 )
							if( Color_con2 <= 2.22769 )
								if( upperBand <= 7.4719 )
									ret := -0.708333 // sell
								if( upperBand > 7.4719 )
									ret := 0.571429
							if( Color_con2 > 2.22769 )
								if( lowerBand <= -0.865295 )
									ret := 0.594595
								if( lowerBand > -0.865295 )
									ret := -0.363636
						if( sDev > 4.7221 )
							if( Color_con1 <= -0.393473 )
								if( Color_con2 <= 4.4668 )
									ret := -0.166667
								if( Color_con2 > 4.4668 )
									ret := 0.500000
							if( Color_con1 > -0.393473 )
								if( midLine <= 2.73582 )
									ret := -0.571429
								if( midLine > 2.73582 )
									ret := -1.000000 // sell
			if( Color_con2 > 4.9195 )
				if( wvf <= 8.06103 )
					if( Color_con2 <= 5.16895 )
						if( sDev <= 4.00852 )
							ret := 0.500000
						if( sDev > 4.00852 )
							ret := 1.000000 // buy
					if( Color_con2 > 5.16895 )
						if( upperBand <= 7.40286 )
							if( upperBand <= 5.50368 )
								if( wvf <= 7.48849 )
									ret := 0.750000 // buy
								if( wvf > 7.48849 )
									ret := -0.750000 // sell
							if( upperBand > 5.50368 )
								ret := -1.000000 // sell
						if( upperBand > 7.40286 )
							ret := 0.285714
				if( wvf > 8.06103 )
					if( Color_con1 <= 3.25501 )
						if( upperBand <= 7.16261 )
							if( lowerBand <= -1.28578 )
								ret := 0.000000
							if( lowerBand > -1.28578 )
								ret := 1.000000 // buy
						if( upperBand > 7.16261 )
							if( midLine <= 2.84291 )
								if( wvf <= 10.8999 )
									ret := 0.700000 // buy
								if( wvf > 10.8999 )
									ret := 1.000000 // buy
							if( midLine > 2.84291 )
								ret := 1.000000 // buy
					if( Color_con1 > 3.25501 )
						if( Color_con1 <= 4.30951 )
							if( midLine <= 1.24346 )
								ret := 1.000000 // buy
							if( midLine > 1.24346 )
								if( upperBand <= 5.37017 )
									ret := -1.000000 // sell
								if( upperBand > 5.37017 )
									ret := -0.200000
						if( Color_con1 > 4.30951 )
							ret := 1.000000 // buy
		if( midLine > 3.43358 )
			if( lowerBand <= 2.84241 )
				if( Color_con1 <= -4.61226 )
					if( upperBand <= 27.321 )
						if( wvf <= 2.5651 )
							if( Color_con1 <= -11.1636 )
								if( lowerBand <= 0.126415 )
									ret := -0.333333
								if( lowerBand > 0.126415 )
									ret := -1.000000 // sell
							if( Color_con1 > -11.1636 )
								if( Color_con2 <= -4.59641 )
									ret := 0.682540
								if( Color_con2 > -4.59641 )
									ret := 0.172414
						if( wvf > 2.5651 )
							if( Color_con1 <= -13.4317 )
								if( midLine <= 11.4821 )
									ret := -0.906977 // sell
								if( midLine > 11.4821 )
									ret := 0.777778 // buy
							if( Color_con1 > -13.4317 )
								if( Color_con2 <= 6.00655 )
									ret := 0.033994
								if( Color_con2 > 6.00655 )
									ret := -0.928571 // sell
					if( upperBand > 27.321 )
						if( lowerBand <= 2.03708 )
							ret := 1.000000 // buy
						if( lowerBand > 2.03708 )
							ret := 0.200000
				if( Color_con1 > -4.61226 )
					if( Color_con1 <= -0.042691 )
						if( sDev <= 5.66476 )
							if( sDev <= 4.42361 )
								if( wvf <= 2.87372 )
									ret := -0.082927
								if( wvf > 2.87372 )
									ret := 0.271700
							if( sDev > 4.42361 )
								if( sDev <= 5.1874 )
									ret := -0.110204
								if( sDev > 5.1874 )
									ret := 0.295082
						if( sDev > 5.66476 )
							if( sDev <= 7.8048 )
								if( Color_con2 <= -0.080886 )
									ret := -0.333333
								if( Color_con2 > -0.080886 )
									ret := 0.642032
							if( sDev > 7.8048 )
								if( upperBand <= 13.252 )
									ret := -0.846154 // sell
								if( upperBand > 13.252 )
									ret := 0.242105
					if( Color_con1 > -0.042691 )
						if( sDev <= 8.42952 )
							if( lowerBand <= 2.2549 )
								if( Color_con2 <= -0.412478 )
									ret := -0.962963 // sell
								if( Color_con2 > -0.412478 )
									ret := -0.155440
							if( lowerBand > 2.2549 )
								if( Color_con2 <= 1.37285 )
									ret := 0.200000
								if( Color_con2 > 1.37285 )
									ret := 0.695652
						if( sDev > 8.42952 )
							if( wvf <= 23.2418 )
								ret := 1.000000 // buy
							if( wvf > 23.2418 )
								ret := 0.750000 // buy
			if( lowerBand > 2.84241 )
				if( upperBand <= 18.2284 )
					if( lowerBand <= 4.88466 )
						if( sDev <= 1.64965 )
							if( lowerBand <= 3.01168 )
								if( midLine <= 3.67032 )
									ret := 0.615385
								if( midLine > 3.67032 )
									ret := -0.515789
							if( lowerBand > 3.01168 )
								if( sDev <= 1.19222 )
									ret := -0.017857
								if( sDev > 1.19222 )
									ret := 0.627219
						if( sDev > 1.64965 )
							if( Color_con1 <= -5.87647 )
								if( sDev <= 5.62444 )
									ret := 0.372973
								if( sDev > 5.62444 )
									ret := -0.476190
							if( Color_con1 > -5.87647 )
								if( lowerBand <= 4.41119 )
									ret := -0.093859
								if( lowerBand > 4.41119 )
									ret := -0.510638
					if( lowerBand > 4.88466 )
						if( sDev <= 4.95943 )
							if( upperBand <= 10.1285 )
								if( midLine <= 6.84987 )
									ret := 0.571429
								if( midLine > 6.84987 )
									ret := 0.000000
							if( upperBand > 10.1285 )
								if( Color_con2 <= -2.73632 )
									ret := 0.400000
								if( Color_con2 > -2.73632 )
									ret := 0.770833 // buy
						if( sDev > 4.95943 )
							if( Color_con1 <= -9.36445 )
								if( Color_con2 <= -8.17565 )
									ret := -0.250000
								if( Color_con2 > -8.17565 )
									ret := 1.000000 // buy
							if( Color_con1 > -9.36445 )
								ret := -1.000000 // sell
				if( upperBand > 18.2284 )
					if( midLine <= 15.7868 )
						if( midLine <= 13.8019 )
							if( Color_con2 <= -1.51006 )
								if( lowerBand <= 4.04857 )
									ret := -0.600000
								if( lowerBand > 4.04857 )
									ret := 0.250000
							if( Color_con2 > -1.51006 )
								ret := 0.666667
						if( midLine > 13.8019 )
							if( midLine <= 15.3704 )
								if( Color_con1 <= -4.51152 )
									ret := -1.000000 // sell
								if( Color_con1 > -4.51152 )
									ret := -0.800000 // sell
							if( midLine > 15.3704 )
								if( midLine <= 15.4513 )
									ret := 0.500000
								if( midLine > 15.4513 )
									ret := -0.750000 // sell
					if( midLine > 15.7868 )
						if( wvf <= 14.9782 )
							if( Color_con2 <= -9.99637 )
								ret := 1.000000 // buy
							if( Color_con2 > -9.99637 )
								if( sDev <= 6.61944 )
									ret := 0.500000
								if( sDev > 6.61944 )
									ret := -0.652174
						if( wvf > 14.9782 )
							if( Color_con2 <= -0.239008 )
								ret := 1.000000 // buy
							if( Color_con2 > -0.239008 )
								ret := 0.500000
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Williams_Vix_Fix 
//@version=5
//indicator "CM_Williams_Vix_Fix", overlay=false)

// Inputs
pd = input.int(22, title="LookBack Period Standard Deviation High")
bbl = input.int(20, title="Bollinger Band Length")
mult = input.float(2.0, minval=1, maxval=5, title="Bollinger Band Standard Deviation Up")
lb = input.int(50, title="Look Back Period Percentile High")
ph = input.float(0.85, title="Highest Percentile - 0.90=90%, 0.95=95%, 0.99=99%")
pl = input.float(1.01, title="Lowest Percentile - 1.10=90%, 1.05=95%, 1.01=99%")
hp = input.bool(false, title="Show High Range - Based on Percentile and LookBack Period?")
sd = input.bool(false, title="Show Standard Deviation Line?")

// Calculations
wvf = ((ta.highest(close, pd) - low) / ta.highest(close, pd)) * 100

sDev = mult * ta.stdev(wvf, bbl)
midLine = ta.sma(wvf, bbl)
lowerBand = midLine - sDev
upperBand = midLine + sDev

rangeHigh = ta.highest(wvf, lb) * ph
rangeLow = ta.lowest(wvf, lb) * pl


Color_con1 = wvf - upperBand
Color_con2 = wvf - rangeHigh
// Color condition
col = wvf >= upperBand or wvf >= rangeHigh ? color.lime : color.gray
colInt = wvf >= upperBand or wvf >= rangeHigh ? 1 : 0 //Bool to int

// Plots
plot(hp and na(rangeHigh) ? na : rangeHigh, title="Range High Percentile", color=color.orange, linewidth=4)
plot(hp and na(rangeLow) ? na : rangeLow, title="Range Low Percentile", color=color.orange, linewidth=4)
plot(wvf, title="Williams Vix Fix", color=col, style=plot.style_histogram, linewidth=4)
plot(sd and na(upperBand) ? na : upperBand, title="Upper Band", color=color.aqua, linewidth=3)

// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_AAVEUSDT_15Min_d35d61b4(rangeHigh, rangeLow, midLine, sDev, lowerBand, wvf, Color_con1, colInt, Color_con2, upperBand)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.


