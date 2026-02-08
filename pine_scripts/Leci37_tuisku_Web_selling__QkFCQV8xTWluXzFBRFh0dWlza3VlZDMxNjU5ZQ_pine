//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: ADX_and_DI
// ID_model: BABA_1Min_1ADX_ed31659e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_BABA_1Min_1ADX_ed31659e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_BABA_1Min_ed31659e(smoothedDirectionalMovementMinus, directionalMovementMinus, diMinus, dx, directionalMovementPlus, smoothedDirectionalMovementPlus, adx, trueRange, smoothedTrueRange, diPlus)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( directionalMovementMinus <= 0.022945 )
		if( directionalMovementPlus <= 0.031104 )
			if( adx <= 51.6807 )
				if( smoothedDirectionalMovementPlus <= 0.05577 )
					if( smoothedTrueRange <= 0.220765 )
						if( smoothedDirectionalMovementMinus <= 0.008577 )
							if( directionalMovementMinus <= 0.001403 )
								if( adx <= 12.8694 )
									ret := 0.096870
								if( adx > 12.8694 )
									ret := -0.015862
							if( directionalMovementMinus > 0.001403 )
								if( directionalMovementPlus <= 0.004965 )
									ret := 0.026904
								if( directionalMovementPlus > 0.004965 )
									ret := 0.192233
						if( smoothedDirectionalMovementMinus > 0.008577 )
							if( diMinus <= 33.7803 )
								if( diPlus <= 19.8658 )
									ret := -0.111297
								if( diPlus > 19.8658 )
									ret := -0.016639
							if( diMinus > 33.7803 )
								if( smoothedDirectionalMovementPlus <= 0.006299 )
									ret := -0.080107
								if( smoothedDirectionalMovementPlus > 0.006299 )
									ret := 0.032464
					if( smoothedTrueRange > 0.220765 )
						if( adx <= 38.7189 )
							if( adx <= 36.8132 )
								if( directionalMovementPlus <= 0.016475 )
									ret := 0.265928
								if( directionalMovementPlus > 0.016475 )
									ret := -0.245283
							if( adx > 36.8132 )
								if( directionalMovementPlus <= 0.000537 )
									ret := -0.612903
								if( directionalMovementPlus > 0.000537 )
									ret := -0.941176 // sell
						if( adx > 38.7189 )
							if( smoothedDirectionalMovementMinus <= 0.115722 )
								if( trueRange <= 0.041947 )
									ret := -0.176471
								if( trueRange > 0.041947 )
									ret := 0.694118
							if( smoothedDirectionalMovementMinus > 0.115722 )
								if( dx <= 69.3272 )
									ret := 0.636364
								if( dx > 69.3272 )
									ret := 0.965517 // buy
				if( smoothedDirectionalMovementPlus > 0.05577 )
					if( diPlus <= 32.0871 )
						if( smoothedDirectionalMovementPlus <= 0.224352 )
							if( smoothedDirectionalMovementMinus <= 0.038295 )
								if( diPlus <= 26.2995 )
									ret := 0.109091
								if( diPlus > 26.2995 )
									ret := -0.660714
							if( smoothedDirectionalMovementMinus > 0.038295 )
								if( diPlus <= 23.7022 )
									ret := -0.016667
								if( diPlus > 23.7022 )
									ret := -0.340909
						if( smoothedDirectionalMovementPlus > 0.224352 )
							ret := -1.000000 // sell
					if( diPlus > 32.0871 )
						if( smoothedDirectionalMovementMinus <= 0.014075 )
							if( diPlus <= 34.8906 )
								if( smoothedTrueRange <= 0.211763 )
									ret := 0.866667 // buy
								if( smoothedTrueRange > 0.211763 )
									ret := 0.454545
							if( diPlus > 34.8906 )
								if( dx <= 77.2931 )
									ret := -0.730000 // sell
								if( dx > 77.2931 )
									ret := -0.196429
						if( smoothedDirectionalMovementMinus > 0.014075 )
							if( smoothedTrueRange <= 0.633801 )
								if( smoothedTrueRange <= 0.37012 )
									ret := 0.056872
								if( smoothedTrueRange > 0.37012 )
									ret := -0.600000
							if( smoothedTrueRange > 0.633801 )
								ret := 1.000000 // buy
			if( adx > 51.6807 )
				if( diPlus <= 80.6496 )
					if( adx <= 65.2672 )
						if( diPlus <= 13.2664 )
							if( dx <= 44.6773 )
								if( diMinus <= 26.9954 )
									ret := 0.247788
								if( diMinus > 26.9954 )
									ret := 0.709677 // buy
							if( dx > 44.6773 )
								if( adx <= 57.4212 )
									ret := 0.043353
								if( adx > 57.4212 )
									ret := 0.296503
						if( diPlus > 13.2664 )
							if( smoothedTrueRange <= 0.693586 )
								if( dx <= 87.2231 )
									ret := 0.002541
								if( dx > 87.2231 )
									ret := 0.409524
							if( smoothedTrueRange > 0.693586 )
								if( smoothedDirectionalMovementMinus <= 0.018891 )
									ret := -0.200000
								if( smoothedDirectionalMovementMinus > 0.018891 )
									ret := -0.939394 // sell
					if( adx > 65.2672 )
						if( smoothedDirectionalMovementMinus <= 0.030336 )
							if( smoothedDirectionalMovementPlus <= 0.004825 )
								if( diMinus <= 25.9848 )
									ret := 0.656716
								if( diMinus > 25.9848 )
									ret := 0.105528
							if( smoothedDirectionalMovementPlus > 0.004825 )
								if( smoothedDirectionalMovementPlus <= 0.099174 )
									ret := -0.007527
								if( smoothedDirectionalMovementPlus > 0.099174 )
									ret := -0.338462
						if( smoothedDirectionalMovementMinus > 0.030336 )
							if( diMinus <= 35.8341 )
								if( diMinus <= 6.52343 )
									ret := -0.687500
								if( diMinus > 6.52343 )
									ret := 0.368794
							if( diMinus > 35.8341 )
								if( dx <= 92.8372 )
									ret := -0.310734
								if( dx > 92.8372 )
									ret := 0.250000
				if( diPlus > 80.6496 )
					if( smoothedTrueRange <= 0.235953 )
						if( smoothedTrueRange <= 0.111425 )
							if( smoothedDirectionalMovementPlus <= 0.070658 )
								if( diMinus <= 3.83439 )
									ret := 0.400000
								if( diMinus > 3.83439 )
									ret := 0.272727
							if( smoothedDirectionalMovementPlus > 0.070658 )
								ret := -0.200000
						if( smoothedTrueRange > 0.111425 )
							if( smoothedTrueRange <= 0.190041 )
								if( smoothedTrueRange <= 0.172571 )
									ret := 0.696203
								if( smoothedTrueRange > 0.172571 )
									ret := 0.233333
							if( smoothedTrueRange > 0.190041 )
								if( adx <= 73.4071 )
									ret := 0.700000 // buy
								if( adx > 73.4071 )
									ret := 1.000000 // buy
					if( smoothedTrueRange > 0.235953 )
						if( directionalMovementPlus <= 0.007055 )
							ret := 0.384615
						if( directionalMovementPlus > 0.007055 )
							ret := -0.187500
		if( directionalMovementPlus > 0.031104 )
			if( diPlus <= 43.4601 )
				if( diPlus <= 2.99487 )
					if( diPlus <= 1.90628 )
						ret := 0.750000 // buy
					if( diPlus > 1.90628 )
						ret := 1.000000 // buy
				if( diPlus > 2.99487 )
					if( smoothedDirectionalMovementPlus <= 0.010559 )
						if( smoothedDirectionalMovementMinus <= 0.09099 )
							if( smoothedDirectionalMovementPlus <= 0.006781 )
								if( trueRange <= 0.069694 )
									ret := 0.062069
								if( trueRange > 0.069694 )
									ret := -0.165517
							if( smoothedDirectionalMovementPlus > 0.006781 )
								if( smoothedDirectionalMovementMinus <= 0.008413 )
									ret := 0.014184
								if( smoothedDirectionalMovementMinus > 0.008413 )
									ret := -0.238556
						if( smoothedDirectionalMovementMinus > 0.09099 )
							ret := 1.000000 // buy
					if( smoothedDirectionalMovementPlus > 0.010559 )
						if( smoothedDirectionalMovementMinus <= 0.010278 )
							if( smoothedDirectionalMovementPlus <= 0.039268 )
								if( dx <= 45.3961 )
									ret := 0.171277
								if( dx > 45.3961 )
									ret := -0.034799
							if( smoothedDirectionalMovementPlus > 0.039268 )
								if( adx <= 64.2587 )
									ret := 0.439446
								if( adx > 64.2587 )
									ret := -0.309524
						if( smoothedDirectionalMovementMinus > 0.010278 )
							if( diMinus <= 8.30394 )
								if( adx <= 57.6934 )
									ret := -0.316981
								if( adx > 57.6934 )
									ret := -0.771429 // sell
							if( diMinus > 8.30394 )
								if( adx <= 48.7331 )
									ret := -0.050771
								if( adx > 48.7331 )
									ret := 0.138545
			if( diPlus > 43.4601 )
				if( smoothedDirectionalMovementMinus <= 0.004598 )
					if( diPlus <= 93.2051 )
						if( adx <= 67.1782 )
							if( adx <= 63.2908 )
								if( diMinus <= 3.66282 )
									ret := -0.099057
								if( diMinus > 3.66282 )
									ret := 0.251627
							if( adx > 63.2908 )
								if( smoothedTrueRange <= 0.106231 )
									ret := 0.771429 // buy
								if( smoothedTrueRange > 0.106231 )
									ret := 0.090909
						if( adx > 67.1782 )
							if( diMinus <= 0.238862 )
								if( smoothedDirectionalMovementPlus <= 0.083204 )
									ret := 0.166667
								if( smoothedDirectionalMovementPlus > 0.083204 )
									ret := 0.909091 // buy
							if( diMinus > 0.238862 )
								if( diMinus <= 0.916136 )
									ret := -0.682927
								if( diMinus > 0.916136 )
									ret := -0.143939
					if( diPlus > 93.2051 )
						if( smoothedDirectionalMovementMinus <= 0.002717 )
							ret := -0.714286 // sell
						if( smoothedDirectionalMovementMinus > 0.002717 )
							ret := -1.000000 // sell
				if( smoothedDirectionalMovementMinus > 0.004598 )
					if( smoothedDirectionalMovementMinus <= 0.014699 )
						if( directionalMovementPlus <= 0.139605 )
							if( adx <= 34.4825 )
								if( adx <= 13.8657 )
									ret := 0.052910
								if( adx > 13.8657 )
									ret := -0.278912
							if( adx > 34.4825 )
								if( smoothedTrueRange <= 0.028071 )
									ret := -0.518519
								if( smoothedTrueRange > 0.028071 )
									ret := 0.056444
						if( directionalMovementPlus > 0.139605 )
							if( dx <= 27.3142 )
								if( dx <= 20.201 )
									ret := 0.428571
								if( dx > 20.201 )
									ret := 0.846154 // buy
							if( dx > 27.3142 )
								if( adx <= 59.7012 )
									ret := -0.347087
								if( adx > 59.7012 )
									ret := -0.911111 // sell
					if( smoothedDirectionalMovementMinus > 0.014699 )
						if( directionalMovementPlus <= 0.037703 )
							if( smoothedDirectionalMovementMinus <= 0.021129 )
								if( trueRange <= 0.036076 )
									ret := -0.888889 // sell
								if( trueRange > 0.036076 )
									ret := -0.280000
							if( smoothedDirectionalMovementMinus > 0.021129 )
								if( smoothedTrueRange <= 0.051912 )
									ret := -1.000000 // sell
								if( smoothedTrueRange > 0.051912 )
									ret := -0.710526 // sell
						if( directionalMovementPlus > 0.037703 )
							if( diMinus <= 10.2465 )
								if( dx <= 73.8758 )
									ret := -0.929825 // sell
								if( dx > 73.8758 )
									ret := -0.390244
							if( diMinus > 10.2465 )
								if( diPlus <= 75.8945 )
									ret := -0.272316
								if( diPlus > 75.8945 )
									ret := -0.965517 // sell
	if( directionalMovementMinus > 0.022945 )
		if( diMinus <= 46.5138 )
			if( diPlus <= 30.0303 )
				if( dx <= 38.9304 )
					if( smoothedTrueRange <= 0.193504 )
						if( smoothedDirectionalMovementMinus <= 0.032025 )
							if( smoothedDirectionalMovementMinus <= 0.024915 )
								if( adx <= 25.3227 )
									ret := -0.103809
								if( adx > 25.3227 )
									ret := 0.004702
							if( smoothedDirectionalMovementMinus > 0.024915 )
								if( dx <= 12.3377 )
									ret := -0.107280
								if( dx > 12.3377 )
									ret := 0.160423
						if( smoothedDirectionalMovementMinus > 0.032025 )
							if( dx <= 18.0677 )
								if( trueRange <= 0.077761 )
									ret := -0.626866
								if( trueRange > 0.077761 )
									ret := -0.010551
							if( dx > 18.0677 )
								if( diPlus <= 18.0615 )
									ret := -0.090778
								if( diPlus > 18.0615 )
									ret := -0.377444
					if( smoothedTrueRange > 0.193504 )
						if( diPlus <= 23.9059 )
							if( dx <= 19.9872 )
								if( dx <= 3.08665 )
									ret := -0.257426
								if( dx > 3.08665 )
									ret := 0.516634
							if( dx > 19.9872 )
								if( smoothedTrueRange <= 0.436525 )
									ret := -0.083744
								if( smoothedTrueRange > 0.436525 )
									ret := 0.954545 // buy
						if( diPlus > 23.9059 )
							if( smoothedDirectionalMovementPlus <= 0.066929 )
								if( diMinus <= 20.5628 )
									ret := -0.225806
								if( diMinus > 20.5628 )
									ret := 0.349206
							if( smoothedDirectionalMovementPlus > 0.066929 )
								if( smoothedDirectionalMovementPlus <= 0.072583 )
									ret := -0.728814 // sell
								if( smoothedDirectionalMovementPlus > 0.072583 )
									ret := -0.320000
				if( dx > 38.9304 )
					if( adx <= 29.3409 )
						if( dx <= 48.5052 )
							if( directionalMovementMinus <= 0.196983 )
								if( smoothedDirectionalMovementPlus <= 0.014886 )
									ret := -0.055944
								if( smoothedDirectionalMovementPlus > 0.014886 )
									ret := 0.256198
							if( directionalMovementMinus > 0.196983 )
								if( smoothedDirectionalMovementMinus <= 0.061611 )
									ret := 0.307692
								if( smoothedDirectionalMovementMinus > 0.061611 )
									ret := 0.933333 // buy
						if( dx > 48.5052 )
							if( smoothedTrueRange <= 0.243791 )
								if( trueRange <= 0.091379 )
									ret := -0.313725
								if( trueRange > 0.091379 )
									ret := 0.026764
							if( smoothedTrueRange > 0.243791 )
								if( directionalMovementMinus <= 0.080465 )
									ret := -1.000000 // sell
								if( directionalMovementMinus > 0.080465 )
									ret := -0.916667 // sell
					if( adx > 29.3409 )
						if( diPlus <= 0.532908 )
							if( directionalMovementMinus <= 0.104346 )
								ret := -0.631579
							if( directionalMovementMinus > 0.104346 )
								ret := -1.000000 // sell
						if( diPlus > 0.532908 )
							if( adx <= 79.2189 )
								if( adx <= 56.0359 )
									ret := 0.130910
								if( adx > 56.0359 )
									ret := 0.370370
							if( adx > 79.2189 )
								if( smoothedDirectionalMovementMinus <= 0.082353 )
									ret := -0.043478
								if( smoothedDirectionalMovementMinus > 0.082353 )
									ret := -0.918919 // sell
			if( diPlus > 30.0303 )
				if( dx <= 23.5341 )
					if( trueRange <= 0.062092 )
						if( smoothedTrueRange <= 0.067079 )
							if( diPlus <= 45.3349 )
								if( diMinus <= 30.1557 )
									ret := 0.128302
								if( diMinus > 30.1557 )
									ret := -0.053245
							if( diPlus > 45.3349 )
								if( diMinus <= 44.2279 )
									ret := 0.307229
								if( diMinus > 44.2279 )
									ret := -0.194805
						if( smoothedTrueRange > 0.067079 )
							if( diPlus <= 38.1485 )
								if( adx <= 15.9656 )
									ret := 0.833333 // buy
								if( adx > 15.9656 )
									ret := -0.012500
							if( diPlus > 38.1485 )
								if( diPlus <= 47.0656 )
									ret := 0.773585 // buy
								if( diPlus > 47.0656 )
									ret := 0.000000
					if( trueRange > 0.062092 )
						if( trueRange <= 0.133216 )
							if( smoothedTrueRange <= 0.121301 )
								if( diPlus <= 42.9287 )
									ret := 0.375274
								if( diPlus > 42.9287 )
									ret := 0.594891
							if( smoothedTrueRange > 0.121301 )
								if( adx <= 32.4677 )
									ret := -0.241935
								if( adx > 32.4677 )
									ret := 0.277778
						if( trueRange > 0.133216 )
							if( diPlus <= 37.115 )
								if( dx <= 21.0813 )
									ret := -0.217703
								if( dx > 21.0813 )
									ret := 0.666667
							if( diPlus > 37.115 )
								if( directionalMovementPlus <= 0.015843 )
									ret := 0.690909
								if( directionalMovementPlus > 0.015843 )
									ret := 0.375000
				if( dx > 23.5341 )
					if( smoothedTrueRange <= 0.599162 )
						if( smoothedDirectionalMovementMinus <= 0.006534 )
							if( adx <= 89.2898 )
								if( directionalMovementPlus <= 0.00464 )
									ret := -0.083168
								if( directionalMovementPlus > 0.00464 )
									ret := -0.505155
							if( adx > 89.2898 )
								ret := 1.000000 // buy
						if( smoothedDirectionalMovementMinus > 0.006534 )
							if( dx <= 74.6777 )
								if( smoothedDirectionalMovementPlus <= 0.199246 )
									ret := 0.086624
								if( smoothedDirectionalMovementPlus > 0.199246 )
									ret := 1.000000 // buy
							if( dx > 74.6777 )
								if( smoothedDirectionalMovementPlus <= 0.218974 )
									ret := 0.626866
								if( smoothedDirectionalMovementPlus > 0.218974 )
									ret := -0.078431
					if( smoothedTrueRange > 0.599162 )
						if( smoothedDirectionalMovementPlus <= 0.474107 )
							ret := -0.083333
						if( smoothedDirectionalMovementPlus > 0.474107 )
							if( dx <= 83.3914 )
								ret := -1.000000 // sell
							if( dx > 83.3914 )
								ret := -0.750000 // sell
		if( diMinus > 46.5138 )
			if( diPlus <= 25.5141 )
				if( smoothedDirectionalMovementPlus <= 0.017859 )
					if( diMinus <= 63.579 )
						if( dx <= 48.8478 )
							if( dx <= 46.1595 )
								if( smoothedDirectionalMovementMinus <= 0.022453 )
									ret := -0.030151
								if( smoothedDirectionalMovementMinus > 0.022453 )
									ret := 0.285714
							if( dx > 46.1595 )
								if( smoothedTrueRange <= 0.046236 )
									ret := -0.068182
								if( smoothedTrueRange > 0.046236 )
									ret := -0.510638
						if( dx > 48.8478 )
							if( adx <= 84.6553 )
								if( directionalMovementMinus <= 0.111525 )
									ret := 0.271084
								if( directionalMovementMinus > 0.111525 )
									ret := 0.561321
							if( adx > 84.6553 )
								if( diPlus <= 4.87238 )
									ret := -1.000000 // sell
								if( diPlus > 4.87238 )
									ret := -0.764706 // sell
					if( diMinus > 63.579 )
						if( smoothedDirectionalMovementMinus <= 0.013914 )
							if( smoothedDirectionalMovementPlus <= 0.002203 )
								if( smoothedDirectionalMovementPlus <= 0.001222 )
									ret := -0.777778 // sell
								if( smoothedDirectionalMovementPlus > 0.001222 )
									ret := 0.142857
							if( smoothedDirectionalMovementPlus > 0.002203 )
								if( diPlus <= 20.8143 )
									ret := -0.913043 // sell
								if( diPlus > 20.8143 )
									ret := -0.312500
						if( smoothedDirectionalMovementMinus > 0.013914 )
							if( adx <= 71.299 )
								if( diPlus <= 12.8572 )
									ret := -0.063395
								if( diPlus > 12.8572 )
									ret := 0.173824
							if( adx > 71.299 )
								if( smoothedDirectionalMovementPlus <= 0.002367 )
									ret := -0.133333
								if( smoothedDirectionalMovementPlus > 0.002367 )
									ret := -0.914286 // sell
				if( smoothedDirectionalMovementPlus > 0.017859 )
					if( trueRange <= 1.773 )
						if( diMinus <= 48.1338 )
							if( dx <= 64.2286 )
								if( diMinus <= 47.5958 )
									ret := 0.280000
								if( diMinus > 47.5958 )
									ret := 0.916667 // buy
							if( dx > 64.2286 )
								ret := -0.428571
						if( diMinus > 48.1338 )
							if( trueRange <= 0.451239 )
								if( diPlus <= 8.84924 )
									ret := 0.200000
								if( diPlus > 8.84924 )
									ret := -0.551601
							if( trueRange > 0.451239 )
								if( trueRange <= 0.494475 )
									ret := 0.800000 // buy
								if( trueRange > 0.494475 )
									ret := -0.051724
					if( trueRange > 1.773 )
						ret := -0.960000 // sell
			if( diPlus > 25.5141 )
				if( smoothedDirectionalMovementMinus <= 0.023827 )
					if( trueRange <= 0.066649 )
						if( diPlus <= 26.9268 )
							if( dx <= 44.4479 )
								if( smoothedDirectionalMovementPlus <= 0.009286 )
									ret := 0.366667
								if( smoothedDirectionalMovementPlus > 0.009286 )
									ret := 1.000000 // buy
							if( dx > 44.4479 )
								ret := 1.000000 // buy
						if( diPlus > 26.9268 )
							if( diMinus <= 47.5406 )
								if( directionalMovementMinus <= 0.03827 )
									ret := 0.085106
								if( directionalMovementMinus > 0.03827 )
									ret := 0.586207
							if( diMinus > 47.5406 )
								if( directionalMovementPlus <= 0.006829 )
									ret := 0.049716
								if( directionalMovementPlus > 0.006829 )
									ret := 0.600000
					if( trueRange > 0.066649 )
						if( adx <= 14.4005 )
							if( diMinus <= 47.1686 )
								ret := 0.500000
							if( diMinus > 47.1686 )
								if( dx <= 30.218 )
									ret := 0.855670 // buy
								if( dx > 30.218 )
									ret := 0.545455
						if( adx > 14.4005 )
							if( diMinus <= 47.3153 )
								ret := -0.611111
							if( diMinus > 47.3153 )
								if( smoothedDirectionalMovementMinus <= 0.022008 )
									ret := 0.513699
								if( smoothedDirectionalMovementMinus > 0.022008 )
									ret := 0.104167
				if( smoothedDirectionalMovementMinus > 0.023827 )
					if( dx <= 25.7893 )
						if( adx <= 52.8209 )
							if( adx <= 15.5405 )
								if( dx <= 2.26987 )
									ret := 0.076923
								if( dx > 2.26987 )
									ret := 0.837037 // buy
							if( adx > 15.5405 )
								if( directionalMovementPlus <= 0.001985 )
									ret := 0.413502
								if( directionalMovementPlus > 0.001985 )
									ret := 0.906977 // buy
						if( adx > 52.8209 )
							ret := -0.285714
					if( dx > 25.7893 )
						if( smoothedDirectionalMovementPlus <= 0.02052 )
							if( diPlus <= 30.7823 )
								if( directionalMovementMinus <= 0.050221 )
									ret := 0.298246
								if( directionalMovementMinus > 0.050221 )
									ret := 0.761905 // buy
							if( diPlus > 30.7823 )
								if( adx <= 35.5729 )
									ret := 0.395349
								if( adx > 35.5729 )
									ret := -0.857143 // sell
						if( smoothedDirectionalMovementPlus > 0.02052 )
							if( diMinus <= 58.7256 )
								if( smoothedTrueRange <= 0.088956 )
									ret := 0.833333 // buy
								if( smoothedTrueRange > 0.088956 )
									ret := -0.296296
							if( diMinus > 58.7256 )
								if( diPlus <= 29.8701 )
									ret := -0.956522 // sell
								if( diPlus > 29.8701 )
									ret := -0.333333
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator ADX_and_DI 
//@version=5
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © BeikabuOyaji

//indicator "ADX and DI for v5", overlay=false)

// Input parameters
len = input(14, title="Length")
th = input(20, title="Threshold")

// Calculate True Range
trueRange = math.max(math.max(high - low, math.abs(high - nz(close[1]))), math.abs(low - nz(close[1])))

// Calculate Directional Movements
directionalMovementPlus = high - nz(high[1]) > nz(low[1]) - low ? math.max(high - nz(high[1]), 0) : 0
directionalMovementMinus = nz(low[1]) - low > high - nz(high[1]) ? math.max(nz(low[1]) - low, 0) : 0

// Initialize and calculate smoothed values
var float smoothedTrueRange = 0
var float smoothedDirectionalMovementPlus = 0
var float smoothedDirectionalMovementMinus = 0

smoothedTrueRange := nz(smoothedTrueRange[1]) - (nz(smoothedTrueRange[1]) / len) + trueRange
smoothedDirectionalMovementPlus := nz(smoothedDirectionalMovementPlus[1]) - (nz(smoothedDirectionalMovementPlus[1]) / len) + directionalMovementPlus
smoothedDirectionalMovementMinus := nz(smoothedDirectionalMovementMinus[1]) - (nz(smoothedDirectionalMovementMinus[1]) / len) + directionalMovementMinus

// Calculate DI+ and DI-
diPlus = (smoothedDirectionalMovementPlus / smoothedTrueRange) * 100
diMinus = (smoothedDirectionalMovementMinus / smoothedTrueRange) * 100

// Calculate DX and ADX
dx = math.abs(diPlus - diMinus) / (diPlus + diMinus) * 100
adx = ta.sma(dx, len)

// Plot DI+, DI-, and ADX
plot(diPlus, color=color.green, title="DI+")
plot(diMinus, color=color.red, title="DI-")
plot(adx, color=color.navy, title="ADX")

// Plot threshold line
hline(th, "Threshold", color=color.black)

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
float op_operation = decision_tree_0_BABA_1Min_ed31659e(smoothedDirectionalMovementMinus, directionalMovementMinus, diMinus, dx, directionalMovementPlus, smoothedDirectionalMovementPlus, adx, trueRange, smoothedTrueRange, diPlus)

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


