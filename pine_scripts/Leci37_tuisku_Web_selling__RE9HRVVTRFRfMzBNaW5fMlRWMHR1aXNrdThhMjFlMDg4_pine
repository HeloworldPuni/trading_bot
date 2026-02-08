//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA, L_Vortex_Indicator
// ID_model: DOGEUSDT_30Min_2TV0_8a21e088 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DOGEUSDT_30Min_2TV0_8a21e088", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DOGEUSDT_30Min_8a21e088(ema12, ema3, ema13, tema, ema1, ema2, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( ema12 <= -0.001372 )
		if( tema <= 0.456376 )
			if( ema2 <= 0.089111 )
				if( ema1 <= 0.068535 )
					if( ema3 <= 0.05921 )
						if( ema3 <= 0.051206 )
							if( VIP_VIM <= -0.344981 )
								if( ema12 <= -0.003302 )
									ret := -0.333333
								if( ema12 > -0.003302 )
									ret := 0.880952 // buy
							if( VIP_VIM > -0.344981 )
								if( ema13 <= -0.002238 )
									ret := -0.458333
								if( ema13 > -0.002238 )
									ret := 1.000000 // buy
						if( ema3 > 0.051206 )
							if( ema12 <= -0.0019 )
								if( ema13 <= -0.002549 )
									ret := 1.000000 // buy
								if( ema13 > -0.002549 )
									ret := 0.750000 // buy
							if( ema12 > -0.0019 )
								if( ema1 <= 0.04996 )
									ret := 0.200000
								if( ema1 > 0.04996 )
									ret := 0.812500 // buy
					if( ema3 > 0.05921 )
						if( tema <= 0.062145 )
							if( VIP <= 0.634072 )
								ret := 0.857143 // buy
							if( VIP > 0.634072 )
								if( VIM <= 1.23651 )
									ret := -0.730769 // sell
								if( VIM > 1.23651 )
									ret := -0.250000
						if( tema > 0.062145 )
							if( ema13 <= -0.002787 )
								if( VIP_VIM <= -0.774864 )
									ret := -0.200000
								if( VIP_VIM > -0.774864 )
									ret := -0.500000
							if( ema13 > -0.002787 )
								if( ema13 <= -0.002216 )
									ret := 0.705882 // buy
								if( ema13 > -0.002216 )
									ret := -0.250000
				if( ema1 > 0.068535 )
					if( ema13 <= -0.002362 )
						if( VIP_VIM <= -0.7872 )
							if( ema2 <= 0.082506 )
								if( ema1 <= 0.071721 )
									ret := 1.000000 // buy
								if( ema1 > 0.071721 )
									ret := 0.222222
							if( ema2 > 0.082506 )
								ret := -0.750000 // sell
						if( VIP_VIM > -0.7872 )
							if( ema13 <= -0.004606 )
								if( ema1 <= 0.085932 )
									ret := 0.944444 // buy
								if( ema1 > 0.085932 )
									ret := 0.500000
							if( ema13 > -0.004606 )
								if( tema <= 0.080257 )
									ret := 0.747475 // buy
								if( tema > 0.080257 )
									ret := 0.465517
					if( ema13 > -0.002362 )
						if( ema13 <= -0.002234 )
							if( ema2 <= 0.087122 )
								if( ema1 <= 0.073436 )
									ret := 0.000000
								if( ema1 > 0.073436 )
									ret := -0.777778 // sell
							if( ema2 > 0.087122 )
								ret := 0.500000
						if( ema13 > -0.002234 )
							if( VIP <= 0.501114 )
								ret := 1.000000 // buy
							if( VIP > 0.501114 )
								if( tema <= 0.081868 )
									ret := 0.000000
								if( tema > 0.081868 )
									ret := 1.000000 // buy
			if( ema2 > 0.089111 )
				if( ema1 <= 0.0937 )
					if( ema2 <= 0.09438 )
						if( VIM <= 1.31714 )
							if( ema13 <= -0.003905 )
								if( VIP <= 0.831315 )
									ret := -1.000000 // sell
								if( VIP > 0.831315 )
									ret := -0.500000
							if( ema13 > -0.003905 )
								if( ema13 <= -0.003299 )
									ret := 0.833333 // buy
								if( ema13 > -0.003299 )
									ret := -0.285714
						if( VIM > 1.31714 )
							if( VIM <= 1.34857 )
								if( tema <= 0.087304 )
									ret := 0.750000 // buy
								if( tema > 0.087304 )
									ret := 1.000000 // buy
							if( VIM > 1.34857 )
								if( tema <= 0.087129 )
									ret := 0.250000
								if( tema > 0.087129 )
									ret := 0.000000
					if( ema2 > 0.09438 )
						if( VIM <= 1.19009 )
							ret := -0.500000
						if( VIM > 1.19009 )
							ret := -1.000000 // sell
				if( ema1 > 0.0937 )
					if( ema3 <= 0.30637 )
						if( ema1 <= 0.285551 )
							if( ema1 <= 0.259814 )
								if( VIP <= 0.930044 )
									ret := 0.236311
								if( VIP > 0.930044 )
									ret := 0.556098
							if( ema1 > 0.259814 )
								if( ema3 <= 0.287167 )
									ret := -0.053521
								if( ema3 > 0.287167 )
									ret := 0.435484
						if( ema1 > 0.285551 )
							if( VIM <= 1.25695 )
								if( VIP <= 0.668181 )
									ret := -0.500000
								if( VIP > 0.668181 )
									ret := 0.600000
							if( VIM > 1.25695 )
								if( ema1 <= 0.28734 )
									ret := 1.000000 // buy
								if( ema1 > 0.28734 )
									ret := -0.333333
					if( ema3 > 0.30637 )
						if( ema12 <= -0.01419 )
							if( ema13 <= -0.031906 )
								ret := 1.000000 // buy
							if( ema13 > -0.031906 )
								if( VIM <= 1.22133 )
									ret := 0.869565 // buy
								if( VIM > 1.22133 )
									ret := 0.000000
						if( ema12 > -0.01419 )
							if( VIP <= 0.91006 )
								if( VIP_VIM <= -0.220132 )
									ret := 0.103641
								if( VIP_VIM > -0.220132 )
									ret := 0.723810 // buy
							if( VIP > 0.91006 )
								if( ema2 <= 0.362676 )
									ret := -0.414894
								if( ema2 > 0.362676 )
									ret := 0.081818
		if( tema > 0.456376 )
			if( VIM <= 1.10296 )
				if( VIP <= 1.04379 )
					if( VIP_VIM <= -0.171819 )
						if( VIP <= 0.834822 )
							if( ema12 <= -0.006432 )
								ret := 0.600000
							if( ema12 > -0.006432 )
								ret := -0.500000
						if( VIP > 0.834822 )
							if( ema13 <= -0.012865 )
								ret := -1.000000 // sell
							if( ema13 > -0.012865 )
								if( VIM <= 1.09077 )
									ret := -0.861111 // sell
								if( VIM > 1.09077 )
									ret := -0.357143
					if( VIP_VIM > -0.171819 )
						if( ema12 <= -0.003437 )
							if( VIP <= 0.934409 )
								if( ema12 <= -0.007068 )
									ret := -0.625000
								if( ema12 > -0.007068 )
									ret := 0.829268 // buy
							if( VIP > 0.934409 )
								if( VIP_VIM <= -0.099644 )
									ret := -0.800000 // sell
								if( VIP_VIM > -0.099644 )
									ret := 0.227273
						if( ema12 > -0.003437 )
							if( ema3 <= 0.516303 )
								if( VIP <= 0.929863 )
									ret := -1.000000 // sell
								if( VIP > 0.929863 )
									ret := -0.031250
							if( ema3 > 0.516303 )
								if( ema3 <= 0.612002 )
									ret := -0.950000 // sell
								if( ema3 > 0.612002 )
									ret := -0.636364
				if( VIP > 1.04379 )
					if( ema12 <= -0.003548 )
						ret := 0.750000 // buy
					if( ema12 > -0.003548 )
						ret := 1.000000 // buy
			if( VIM > 1.10296 )
				if( ema13 <= -0.04993 )
					if( ema2 <= 0.612743 )
						ret := -1.000000 // sell
					if( ema2 > 0.612743 )
						ret := -0.500000
				if( ema13 > -0.04993 )
					if( ema1 <= 0.554742 )
						if( tema <= 0.513511 )
							if( VIP_VIM <= -0.49733 )
								ret := -1.000000 // sell
							if( VIP_VIM > -0.49733 )
								if( ema3 <= 0.492086 )
									ret := -0.444444
								if( ema3 > 0.492086 )
									ret := 0.697368
						if( tema > 0.513511 )
							if( VIP <= 0.851327 )
								if( VIP_VIM <= -0.308708 )
									ret := -0.909091 // sell
								if( VIP_VIM > -0.308708 )
									ret := -0.250000
							if( VIP > 0.851327 )
								if( tema <= 0.531682 )
									ret := 0.562500
								if( tema > 0.531682 )
									ret := -0.769231 // sell
					if( ema1 > 0.554742 )
						if( VIM <= 1.11213 )
							ret := 0.250000
						if( VIM > 1.11213 )
							if( ema12 <= -0.007796 )
								if( VIP_VIM <= -0.273253 )
									ret := 1.000000 // buy
								if( VIP_VIM > -0.273253 )
									ret := 0.750000 // buy
							if( ema12 > -0.007796 )
								if( VIP_VIM <= -0.30003 )
									ret := 0.500000
								if( VIP_VIM > -0.30003 )
									ret := 1.000000 // buy
	if( ema12 > -0.001372 )
		if( tema <= 0.078579 )
			if( ema12 <= -0.000301 )
				if( VIM <= 1.22358 )
					if( tema <= 0.048557 )
						if( VIM <= 1.11637 )
							if( ema12 <= -0.001065 )
								ret := 0.714286 // buy
							if( ema12 > -0.001065 )
								if( VIP <= 0.820658 )
									ret := 1.000000 // buy
								if( VIP > 0.820658 )
									ret := -0.580247
						if( VIM > 1.11637 )
							if( tema <= 0.047213 )
								if( tema <= 0.046125 )
									ret := 0.270270
								if( tema > 0.046125 )
									ret := 1.000000 // buy
							if( tema > 0.047213 )
								if( VIP_VIM <= -0.304035 )
									ret := -0.777778 // sell
								if( VIP_VIM > -0.304035 )
									ret := 0.600000
					if( tema > 0.048557 )
						if( ema2 <= 0.076848 )
							if( VIM <= 1.04643 )
								if( ema12 <= -0.000752 )
									ret := 0.842105 // buy
								if( ema12 > -0.000752 )
									ret := -0.104478
							if( VIM > 1.04643 )
								if( ema12 <= -0.001104 )
									ret := -0.169231
								if( ema12 > -0.001104 )
									ret := 0.245079
						if( ema2 > 0.076848 )
							if( VIP_VIM <= -0.306074 )
								if( VIP_VIM <= -0.458193 )
									ret := 0.656250
								if( VIP_VIM > -0.458193 )
									ret := 0.072581
							if( VIP_VIM > -0.306074 )
								if( ema12 <= -0.000323 )
									ret := 0.719745 // buy
								if( ema12 > -0.000323 )
									ret := 0.210526
				if( VIM > 1.22358 )
					if( ema2 <= 0.011605 )
						if( ema13 <= -0.000606 )
							if( tema <= 0.008315 )
								ret := 1.000000 // buy
							if( tema > 0.008315 )
								ret := 0.750000 // buy
						if( ema13 > -0.000606 )
							ret := 0.400000
					if( ema2 > 0.011605 )
						if( ema13 <= -0.001513 )
							if( VIP <= 0.78983 )
								if( ema2 <= 0.063897 )
									ret := 0.592105
								if( ema2 > 0.063897 )
									ret := 0.123932
							if( VIP > 0.78983 )
								if( VIP <= 0.829911 )
									ret := -0.880000 // sell
								if( VIP > 0.829911 )
									ret := 0.250000
						if( ema13 > -0.001513 )
							if( ema1 <= 0.063575 )
								if( VIP <= 0.605028 )
									ret := 0.533333
								if( VIP > 0.605028 )
									ret := -0.269565
							if( ema1 > 0.063575 )
								if( ema2 <= 0.06541 )
									ret := 0.433333
								if( ema2 > 0.06541 )
									ret := 0.000000
			if( ema12 > -0.000301 )
				if( ema2 <= 0.054548 )
					if( ema3 <= 0.002835 )
						if( VIP_VIM <= -0.551874 )
							if( VIP <= 0.700112 )
								if( VIP <= 0.659887 )
									ret := 0.750000 // buy
								if( VIP > 0.659887 )
									ret := 0.166667
							if( VIP > 0.700112 )
								if( VIP <= 0.732118 )
									ret := 1.000000 // buy
								if( VIP > 0.732118 )
									ret := 0.750000 // buy
						if( VIP_VIM > -0.551874 )
							if( ema12 <= -2.4e-05 )
								if( tema <= 0.00265 )
									ret := 0.000000
								if( tema > 0.00265 )
									ret := -0.800000 // sell
							if( ema12 > -2.4e-05 )
								if( VIM <= 0.779206 )
									ret := -0.290323
								if( VIM > 0.779206 )
									ret := 0.025875
					if( ema3 > 0.002835 )
						if( VIP <= 1.27911 )
							if( VIP_VIM <= -0.145251 )
								if( ema13 <= 0.000878 )
									ret := 0.266625
								if( ema13 > 0.000878 )
									ret := -1.000000 // sell
							if( VIP_VIM > -0.145251 )
								if( ema13 <= 0.000871 )
									ret := 0.092771
								if( ema13 > 0.000871 )
									ret := 0.355509
						if( VIP > 1.27911 )
							if( VIP_VIM <= 0.690801 )
								if( ema13 <= 0.000104 )
									ret := -0.500000
								if( ema13 > 0.000104 )
									ret := -0.029412
							if( VIP_VIM > 0.690801 )
								if( VIM <= 0.612076 )
									ret := -0.944444 // sell
								if( VIM > 0.612076 )
									ret := 0.000000
				if( ema2 > 0.054548 )
					if( ema12 <= 0.000849 )
						if( VIP_VIM <= -0.259449 )
							if( VIM <= 1.21872 )
								if( VIP <= 0.778842 )
									ret := 0.063348
								if( VIP > 0.778842 )
									ret := -0.131265
							if( VIM > 1.21872 )
								if( tema <= 0.072846 )
									ret := 0.155629
								if( tema > 0.072846 )
									ret := -0.200000
						if( VIP_VIM > -0.259449 )
							if( ema12 <= -0.000249 )
								if( ema12 <= -0.000271 )
									ret := 0.171569
								if( ema12 > -0.000271 )
									ret := 0.379518
							if( ema12 > -0.000249 )
								if( ema13 <= 3.7e-05 )
									ret := 0.013686
								if( ema13 > 3.7e-05 )
									ret := 0.073311
					if( ema12 > 0.000849 )
						if( VIP_VIM <= 0.505117 )
							if( VIP_VIM <= 0.490018 )
								if( ema12 <= 0.001336 )
									ret := -0.234375
								if( ema12 > 0.001336 )
									ret := 0.173469
							if( VIP_VIM > 0.490018 )
								if( VIP_VIM <= 0.500462 )
									ret := 0.909091 // buy
								if( VIP_VIM > 0.500462 )
									ret := 0.000000
						if( VIP_VIM > 0.505117 )
							if( ema12 <= 0.001298 )
								if( VIP_VIM <= 0.576701 )
									ret := -0.518519
								if( VIP_VIM > 0.576701 )
									ret := -0.020202
							if( ema12 > 0.001298 )
								if( VIM <= 0.646513 )
									ret := -0.611111
								if( VIM > 0.646513 )
									ret := -0.951220 // sell
		if( tema > 0.078579 )
			if( VIM <= 0.692618 )
				if( tema <= 0.16067 )
					if( tema <= 0.110835 )
						if( ema2 <= 0.076386 )
							if( VIP <= 1.25465 )
								if( ema2 <= 0.072356 )
									ret := -1.000000 // sell
								if( ema2 > 0.072356 )
									ret := -0.250000
							if( VIP > 1.25465 )
								ret := -1.000000 // sell
						if( ema2 > 0.076386 )
							if( tema <= 0.088222 )
								if( VIP <= 1.17727 )
									ret := -0.523810
								if( VIP > 1.17727 )
									ret := 0.224359
							if( tema > 0.088222 )
								if( VIM <= 0.639465 )
									ret := -0.443396
								if( VIM > 0.639465 )
									ret := -0.039370
					if( tema > 0.110835 )
						if( VIP <= 1.2745 )
							if( VIP_VIM <= 0.511734 )
								if( ema13 <= 0.001772 )
									ret := 1.000000 // buy
								if( ema13 > 0.001772 )
									ret := -0.166667
							if( VIP_VIM > 0.511734 )
								if( ema3 <= 0.105268 )
									ret := 0.916667 // buy
								if( ema3 > 0.105268 )
									ret := -0.294118
						if( VIP > 1.2745 )
							if( ema13 <= 0.002825 )
								if( tema <= 0.13838 )
									ret := 0.061224
								if( tema > 0.13838 )
									ret := 0.500000
							if( ema13 > 0.002825 )
								if( tema <= 0.14811 )
									ret := 0.786517 // buy
								if( tema > 0.14811 )
									ret := 0.225806
				if( tema > 0.16067 )
					if( ema12 <= 0.016062 )
						if( ema1 <= 0.210517 )
							if( VIM <= 0.616703 )
								if( VIP_VIM <= 0.742257 )
									ret := 0.645161
								if( VIP_VIM > 0.742257 )
									ret := -0.396552
							if( VIM > 0.616703 )
								if( VIP <= 1.24634 )
									ret := -0.051282
								if( VIP > 1.24634 )
									ret := -0.670330
						if( ema1 > 0.210517 )
							if( VIP <= 1.25516 )
								if( ema1 <= 0.327908 )
									ret := -0.530612
								if( ema1 > 0.327908 )
									ret := 0.857143 // buy
							if( VIP > 1.25516 )
								if( VIM <= 0.674728 )
									ret := -0.831858 // sell
								if( VIM > 0.674728 )
									ret := -0.250000
					if( ema12 > 0.016062 )
						if( ema2 <= 0.604572 )
							if( ema12 <= 0.020666 )
								if( ema2 <= 0.421128 )
									ret := 0.250000
								if( ema2 > 0.421128 )
									ret := 1.000000 // buy
							if( ema12 > 0.020666 )
								if( VIP_VIM <= 0.631298 )
									ret := 0.428571
								if( VIP_VIM > 0.631298 )
									ret := -0.818182 // sell
						if( ema2 > 0.604572 )
							ret := -1.000000 // sell
			if( VIM > 0.692618 )
				if( ema13 <= 0.000364 )
					if( ema2 <= 0.325318 )
						if( ema12 <= -0.000406 )
							if( tema <= 0.100677 )
								if( ema1 <= 0.08493 )
									ret := 0.058085
								if( ema1 > 0.08493 )
									ret := 0.239907
							if( tema > 0.100677 )
								if( VIM <= 1.04484 )
									ret := 0.205599
								if( VIM > 1.04484 )
									ret := -0.018287
						if( ema12 > -0.000406 )
							if( ema13 <= -0.000203 )
								if( VIP_VIM <= 0.199828 )
									ret := -0.078321
								if( VIP_VIM > 0.199828 )
									ret := 0.285714
							if( ema13 > -0.000203 )
								if( VIM <= 0.941169 )
									ret := -0.046807
								if( VIM > 0.941169 )
									ret := 0.023707
					if( ema2 > 0.325318 )
						if( ema13 <= -0.00051 )
							if( VIP <= 1.04104 )
								if( ema13 <= -0.006473 )
									ret := 0.266667
								if( ema13 > -0.006473 )
									ret := -0.494152
							if( VIP > 1.04104 )
								if( VIP <= 1.12082 )
									ret := 0.307692
								if( VIP > 1.12082 )
									ret := -0.800000 // sell
						if( ema13 > -0.00051 )
							if( ema2 <= 0.37792 )
								if( VIM <= 0.926733 )
									ret := 0.800000 // buy
								if( VIM > 0.926733 )
									ret := -0.288136
							if( ema2 > 0.37792 )
								if( ema12 <= -0.000973 )
									ret := -0.428571
								if( ema12 > -0.000973 )
									ret := 0.717949 // buy
				if( ema13 > 0.000364 )
					if( VIP_VIM <= 0.182529 )
						if( VIP <= 0.920232 )
							if( VIP_VIM <= -0.229247 )
								if( ema12 <= 0.000117 )
									ret := 0.571429
								if( ema12 > 0.000117 )
									ret := -0.153846
							if( VIP_VIM > -0.229247 )
								if( VIM <= 0.923656 )
									ret := 0.400000
								if( VIM > 0.923656 )
									ret := -0.625000
						if( VIP > 0.920232 )
							if( ema13 <= 0.017735 )
								if( ema13 <= 0.005629 )
									ret := 0.089431
								if( ema13 > 0.005629 )
									ret := 0.341297
							if( ema13 > 0.017735 )
								if( VIM <= 0.923381 )
									ret := 0.750000 // buy
								if( VIM > 0.923381 )
									ret := -0.913043 // sell
					if( VIP_VIM > 0.182529 )
						if( ema1 <= 0.079197 )
							if( VIP <= 1.1918 )
								if( VIM <= 0.811455 )
									ret := 0.761905 // buy
								if( VIM > 0.811455 )
									ret := 0.208333
							if( VIP > 1.1918 )
								if( VIP <= 1.26869 )
									ret := -0.126761
								if( VIP > 1.26869 )
									ret := 0.714286 // buy
						if( ema1 > 0.079197 )
							if( VIP_VIM <= 0.212101 )
								if( ema3 <= 0.350709 )
									ret := -0.149166
								if( ema3 > 0.350709 )
									ret := 0.540541
							if( VIP_VIM > 0.212101 )
								if( ema1 <= 0.114893 )
									ret := -0.039138
								if( ema1 > 0.114893 )
									ret := 0.050176
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Triple_EMA 
//@version=5
//indicator title="Triple EMA", shorttitle="TEMA", overlay=true, timeframe="", timeframe_gaps=true)
length_TEMA = input.int(9, minval=1)
ema1 = ta.ema(close, length_TEMA)
ema2 = ta.ema(ema1, length_TEMA)
ema3 = ta.ema(ema2, length_TEMA)
tema = 3 * (ema1 - ema2) + ema3
plot(tema, "TEMA", color=#2962FF)

ema12 = ema1 - ema2
ema13 = ema1 - ema3



//CODE associated with the technical indicator L_Vortex_Indicator 
//@version=5
//indicator title = "Vortex Indicator", shorttitle="VI", format=format.price, precision=4, timeframe="", timeframe_gaps=true)
period_ = input.int(14, title="Length", minval=2)
VMP = math.sum( math.abs( high - low[1]), period_ )
VMM = math.sum( math.abs( low - high[1]), period_ )
STR = math.sum( ta.atr(1), period_ )
VIP = VMP / STR
VIM = VMM / STR

VIP_VIM = VIP - VIM

plot(VIP, title="VI +", color=#2962FF)
plot(VIM, title="VI -", color=#E91E63)
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
float op_operation = decision_tree_0_DOGEUSDT_30Min_8a21e088(ema12, ema3, ema13, tema, ema1, ema2, VIP, VIP_VIM, VIM)

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


