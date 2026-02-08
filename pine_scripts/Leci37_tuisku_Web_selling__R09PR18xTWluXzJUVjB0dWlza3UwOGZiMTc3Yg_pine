//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA, L_Vortex_Indicator
// ID_model: GOOG_1Min_2TV0_08fb177b Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_GOOG_1Min_2TV0_08fb177b", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_GOOG_1Min_08fb177b(ema12, ema3, ema13, tema, ema1, ema2, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( ema12 <= 0.015152 )
		if( ema1 <= 158.118 )
			if( ema3 <= 157.7 )
				if( VIM <= 1.76899 )
					if( ema13 <= -0.450381 )
						if( VIM <= 1.42 )
							if( ema2 <= 153.39 )
								if( ema1 <= 151.054 )
									ret := -0.631579
								if( ema1 > 151.054 )
									ret := -1.000000 // sell
							if( ema2 > 153.39 )
								if( ema3 <= 157.05 )
									ret := 0.416667
								if( ema3 > 157.05 )
									ret := -0.300000
						if( VIM > 1.42 )
							if( ema13 <= -0.604942 )
								ret := 0.736842 // buy
							if( ema13 > -0.604942 )
								ret := -0.066667
					if( ema13 > -0.450381 )
						if( VIP_VIM <= -0.789442 )
							if( ema13 <= -0.378551 )
								ret := -1.000000 // sell
							if( ema13 > -0.378551 )
								if( VIM <= 1.54674 )
									ret := -0.086957
								if( VIM > 1.54674 )
									ret := -0.863636 // sell
						if( VIP_VIM > -0.789442 )
							if( VIP <= 0.820738 )
								if( tema <= 148.42 )
									ret := 1.000000 // buy
								if( tema > 148.42 )
									ret := 0.186076
							if( VIP > 0.820738 )
								if( ema13 <= -0.107593 )
									ret := -0.176647
								if( ema13 > -0.107593 )
									ret := 0.064612
				if( VIM > 1.76899 )
					if( VIP_VIM <= -0.582441 )
						if( ema1 <= 156.393 )
							if( ema13 <= 0.016358 )
								if( VIP <= 0.949648 )
									ret := 0.000000
								if( VIP > 0.949648 )
									ret := 0.827411 // buy
							if( ema13 > 0.016358 )
								ret := -0.777778 // sell
						if( ema1 > 156.393 )
							if( ema13 <= -0.292001 )
								if( VIP <= 3.61584 )
									ret := -1.000000 // sell
								if( VIP > 3.61584 )
									ret := -0.800000 // sell
							if( ema13 > -0.292001 )
								if( VIM <= 2.28767 )
									ret := 0.148148
								if( VIM > 2.28767 )
									ret := 0.622642
					if( VIP_VIM > -0.582441 )
						if( ema3 <= 152.793 )
							if( VIM <= 2.31912 )
								if( VIM <= 2.12759 )
									ret := 0.605263
								if( VIM > 2.12759 )
									ret := -0.391304
							if( VIM > 2.31912 )
								if( VIM <= 5.37649 )
									ret := 0.819444 // buy
								if( VIM > 5.37649 )
									ret := 0.229167
						if( ema3 > 152.793 )
							if( ema3 <= 153.351 )
								if( ema1 <= 152.969 )
									ret := -0.333333
								if( ema1 > 152.969 )
									ret := -1.000000 // sell
							if( ema3 > 153.351 )
								if( ema13 <= -0.102673 )
									ret := 0.567901
								if( ema13 > -0.102673 )
									ret := -0.033708
			if( ema3 > 157.7 )
				if( VIM <= 1.11213 )
					if( ema2 <= 157.738 )
						if( ema13 <= -0.086687 )
							ret := -0.500000
						if( ema13 > -0.086687 )
							if( ema13 <= -0.022149 )
								if( ema1 <= 157.697 )
									ret := 0.653846
								if( ema1 > 157.697 )
									ret := 1.000000 // buy
							if( ema13 > -0.022149 )
								if( tema <= 157.73 )
									ret := 0.000000
								if( tema > 157.73 )
									ret := 0.785714 // buy
					if( ema2 > 157.738 )
						if( VIP_VIM <= -0.173738 )
							if( ema12 <= -0.110987 )
								ret := 1.000000 // buy
							if( ema12 > -0.110987 )
								ret := -0.150000
						if( VIP_VIM > -0.173738 )
							if( ema13 <= -0.08762 )
								if( tema <= 157.83 )
									ret := -1.000000 // sell
								if( tema > 157.83 )
									ret := -0.500000
							if( ema13 > -0.08762 )
								if( VIM <= 1.0534 )
									ret := -0.250000
								if( VIM > 1.0534 )
									ret := 0.190476
				if( VIM > 1.11213 )
					if( ema3 <= 158.277 )
						if( ema2 <= 158.114 )
							if( ema1 <= 157.88 )
								if( ema1 <= 157.864 )
									ret := 0.595442
								if( ema1 > 157.864 )
									ret := 1.000000 // buy
							if( ema1 > 157.88 )
								if( VIP <= 0.789341 )
									ret := -0.789474 // sell
								if( VIP > 0.789341 )
									ret := 0.485944
						if( ema2 > 158.114 )
							if( tema <= 157.919 )
								ret := -0.772727 // sell
							if( tema > 157.919 )
								if( ema2 <= 158.17 )
									ret := 0.521739
								if( ema2 > 158.17 )
									ret := -0.400000
					if( ema3 > 158.277 )
						if( ema2 <= 158.413 )
							if( VIM <= 5.03134 )
								if( ema13 <= -0.223593 )
									ret := 0.989130 // buy
								if( ema13 > -0.223593 )
									ret := 0.909091 // buy
							if( VIM > 5.03134 )
								ret := 0.545455
						if( ema2 > 158.413 )
							ret := 0.400000
		if( ema1 > 158.118 )
			if( ema13 <= -0.595607 )
				if( tema <= 173.375 )
					if( VIP_VIM <= -0.636935 )
						if( ema12 <= -1.04194 )
							ret := 1.000000 // buy
						if( ema12 > -1.04194 )
							if( tema <= 172.35 )
								if( ema13 <= -0.919826 )
									ret := -0.619355
								if( ema13 > -0.919826 )
									ret := 0.033639
							if( tema > 172.35 )
								if( VIM <= 1.70164 )
									ret := 1.000000 // buy
								if( VIM > 1.70164 )
									ret := 0.727273 // buy
					if( VIP_VIM > -0.636935 )
						if( VIM <= 2.188 )
							if( ema2 <= 171.167 )
								if( tema <= 168.046 )
									ret := -0.545775
								if( tema > 168.046 )
									ret := 0.071429
							if( ema2 > 171.167 )
								if( ema12 <= -0.422874 )
									ret := -0.612903
								if( ema12 > -0.422874 )
									ret := -0.947368 // sell
						if( VIM > 2.188 )
							if( ema3 <= 164.624 )
								ret := 1.000000 // buy
							if( ema3 > 164.624 )
								if( VIP_VIM <= -0.530337 )
									ret := 0.533333
								if( VIP_VIM > -0.530337 )
									ret := -0.933333 // sell
				if( tema > 173.375 )
					if( tema <= 178.016 )
						if( VIP_VIM <= -0.419635 )
							if( ema3 <= 176.496 )
								ret := 1.000000 // buy
							if( ema3 > 176.496 )
								if( ema12 <= -0.361328 )
									ret := 0.785714 // buy
								if( ema12 > -0.361328 )
									ret := 1.000000 // buy
						if( VIP_VIM > -0.419635 )
							ret := 0.750000 // buy
					if( tema > 178.016 )
						if( ema2 <= 184.25 )
							if( ema2 <= 183.545 )
								if( VIM <= 1.30836 )
									ret := 0.468750
								if( VIM > 1.30836 )
									ret := -0.416667
							if( ema2 > 183.545 )
								if( VIP <= 0.66687 )
									ret := 0.578947
								if( VIP > 0.66687 )
									ret := 1.000000 // buy
						if( ema2 > 184.25 )
							if( VIM <= 1.36014 )
								if( ema12 <= -0.435536 )
									ret := -0.619048
								if( ema12 > -0.435536 )
									ret := -1.000000 // sell
							if( VIM > 1.36014 )
								ret := 0.538462
			if( ema13 > -0.595607 )
				if( ema12 <= -0.109447 )
					if( VIP <= 0.808408 )
						if( VIM <= 1.17162 )
							if( VIM <= 1.06291 )
								ret := 0.142857
							if( VIM > 1.06291 )
								if( tema <= 180.667 )
									ret := -0.457516
								if( tema > 180.667 )
									ret := -0.791667 // sell
						if( VIM > 1.17162 )
							if( tema <= 172.67 )
								if( ema2 <= 171.19 )
									ret := 0.069422
								if( ema2 > 171.19 )
									ret := 0.492114
							if( tema > 172.67 )
								if( tema <= 177.052 )
									ret := -0.264580
								if( tema > 177.052 )
									ret := 0.039308
					if( VIP > 0.808408 )
						if( ema2 <= 191.117 )
							if( VIM <= 1.07528 )
								if( ema1 <= 164.277 )
									ret := 0.621212
								if( ema1 > 164.277 )
									ret := -0.252226
							if( VIM > 1.07528 )
								if( ema12 <= -0.353688 )
									ret := -0.705882 // sell
								if( ema12 > -0.353688 )
									ret := 0.241411
						if( ema2 > 191.117 )
							if( ema3 <= 191.518 )
								ret := -1.000000 // sell
							if( ema3 > 191.518 )
								if( VIP_VIM <= -0.796667 )
									ret := 0.076923
								if( VIP_VIM > -0.796667 )
									ret := -0.685714
				if( ema12 > -0.109447 )
					if( VIP <= 0.92673 )
						if( ema1 <= 187.35 )
							if( ema3 <= 186.653 )
								if( ema1 <= 185.462 )
									ret := -0.026669
								if( ema1 > 185.462 )
									ret := -0.307985
							if( ema3 > 186.653 )
								if( tema <= 186.669 )
									ret := 0.906977 // buy
								if( tema > 186.669 )
									ret := 0.146341
						if( ema1 > 187.35 )
							if( ema2 <= 187.877 )
								if( ema1 <= 187.745 )
									ret := -0.656250
								if( ema1 > 187.745 )
									ret := -1.000000 // sell
							if( ema2 > 187.877 )
								if( ema1 <= 190.312 )
									ret := -0.266917
								if( ema1 > 190.312 )
									ret := 0.031579
					if( VIP > 0.92673 )
						if( ema1 <= 191.972 )
							if( ema3 <= 182.044 )
								if( ema13 <= -0.095315 )
									ret := 0.094675
								if( ema13 > -0.095315 )
									ret := 0.013875
							if( ema3 > 182.044 )
								if( ema2 <= 183.71 )
									ret := 0.531590
								if( ema2 > 183.71 )
									ret := 0.076080
						if( ema1 > 191.972 )
							if( VIP <= 1.83452 )
								if( VIM <= 1.025 )
									ret := -0.250000
								if( VIM > 1.025 )
									ret := -0.722222 // sell
							if( VIP > 1.83452 )
								if( VIM <= 41.25 )
									ret := 0.285714
								if( VIM > 41.25 )
									ret := -0.625000
	if( ema12 > 0.015152 )
		if( VIP <= 1.59766 )
			if( tema <= 150.152 )
				if( ema13 <= 0.25825 )
					if( tema <= 149.455 )
						if( ema12 <= 0.065912 )
							ret := 0.923077 // buy
						if( ema12 > 0.065912 )
							ret := 1.000000 // buy
					if( tema > 149.455 )
						if( ema2 <= 149.551 )
							ret := 0.045455
						if( ema2 > 149.551 )
							if( ema12 <= 0.062537 )
								if( VIP <= 1.16664 )
									ret := 0.661538
								if( VIP > 1.16664 )
									ret := -0.040000
							if( ema12 > 0.062537 )
								if( VIP_VIM <= 0.323817 )
									ret := 0.818182 // buy
								if( VIP_VIM > 0.323817 )
									ret := 1.000000 // buy
				if( ema13 > 0.25825 )
					if( ema2 <= 149.48 )
						if( ema13 <= 0.298958 )
							ret := 0.230769
						if( ema13 > 0.298958 )
							ret := -0.214286
					if( ema2 > 149.48 )
						ret := -0.833333 // sell
			if( tema > 150.152 )
				if( VIM <= 0.844289 )
					if( tema <= 166.989 )
						if( ema1 <= 166.017 )
							if( ema12 <= 0.238276 )
								if( tema <= 164.192 )
									ret := 0.189518
								if( tema > 164.192 )
									ret := 0.006446
							if( ema12 > 0.238276 )
								if( ema12 <= 0.838605 )
									ret := -0.317778
								if( ema12 > 0.838605 )
									ret := 1.000000 // buy
						if( ema1 > 166.017 )
							if( VIM <= 0.80203 )
								if( ema2 <= 166.095 )
									ret := 0.093023
								if( ema2 > 166.095 )
									ret := 0.657534
							if( VIM > 0.80203 )
								if( tema <= 166.261 )
									ret := 0.941176 // buy
								if( tema > 166.261 )
									ret := -0.039216
					if( tema > 166.989 )
						if( ema1 <= 184.167 )
							if( tema <= 177.527 )
								if( ema1 <= 177.224 )
									ret := -0.014203
								if( ema1 > 177.224 )
									ret := 0.539130
							if( tema > 177.527 )
								if( VIP <= 1.28109 )
									ret := -0.071535
								if( VIP > 1.28109 )
									ret := -0.439499
						if( ema1 > 184.167 )
							if( ema2 <= 190.727 )
								if( ema2 <= 185.81 )
									ret := 0.354244
								if( ema2 > 185.81 )
									ret := 0.098748
							if( ema2 > 190.727 )
								if( ema2 <= 192.174 )
									ret := -0.314879
								if( ema2 > 192.174 )
									ret := 0.111111
				if( VIM > 0.844289 )
					if( ema1 <= 179.814 )
						if( VIP_VIM <= -0.143654 )
							if( VIP <= 1.53465 )
								if( tema <= 171.205 )
									ret := -0.474576
								if( tema > 171.205 )
									ret := -0.089655
							if( VIP > 1.53465 )
								if( ema2 <= 162.202 )
									ret := 0.714286 // buy
								if( ema2 > 162.202 )
									ret := 0.000000
						if( VIP_VIM > -0.143654 )
							if( ema13 <= 0.208296 )
								if( tema <= 151.228 )
									ret := 0.300000
								if( tema > 151.228 )
									ret := -0.027033
							if( ema13 > 0.208296 )
								if( tema <= 178.642 )
									ret := -0.184254
								if( tema > 178.642 )
									ret := 0.614754
					if( ema1 > 179.814 )
						if( ema3 <= 181.249 )
							if( ema12 <= 0.034596 )
								if( ema2 <= 180.657 )
									ret := 0.384615
								if( ema2 > 180.657 )
									ret := -0.295775
							if( ema12 > 0.034596 )
								if( VIP_VIM <= 0.355761 )
									ret := -0.604294
								if( VIP_VIM > 0.355761 )
									ret := 0.428571
						if( ema3 > 181.249 )
							if( ema2 <= 182.592 )
								if( ema2 <= 182.258 )
									ret := 0.075099
								if( ema2 > 182.258 )
									ret := 0.695652
							if( ema2 > 182.592 )
								if( ema1 <= 182.82 )
									ret := -0.648148
								if( ema1 > 182.82 )
									ret := -0.157324
		if( VIP > 1.59766 )
			if( VIP_VIM <= 1.4658 )
				if( VIP_VIM <= -0.153564 )
					if( tema <= 184.375 )
						if( ema13 <= 0.107325 )
							if( VIP_VIM <= -0.396153 )
								if( tema <= 183.946 )
									ret := -0.184949
								if( tema > 183.946 )
									ret := -0.952381 // sell
							if( VIP_VIM > -0.396153 )
								if( tema <= 153.397 )
									ret := -0.647059
								if( tema > 153.397 )
									ret := 0.120743
						if( ema13 > 0.107325 )
							if( ema2 <= 171.096 )
								if( ema1 <= 169.405 )
									ret := 0.127321
								if( ema1 > 169.405 )
									ret := 0.864865 // buy
							if( ema2 > 171.096 )
								if( ema12 <= 0.091674 )
									ret := 0.031250
								if( ema12 > 0.091674 )
									ret := -0.656250
					if( tema > 184.375 )
						if( ema1 <= 192.31 )
							if( ema1 <= 188.394 )
								if( ema2 <= 187.021 )
									ret := 0.233333
								if( ema2 > 187.021 )
									ret := 0.882353 // buy
							if( ema1 > 188.394 )
								if( ema13 <= 0.090906 )
									ret := 0.400000
								if( ema13 > 0.090906 )
									ret := -0.300000
						if( ema1 > 192.31 )
							if( tema <= 192.59 )
								ret := 1.000000 // buy
							if( tema > 192.59 )
								ret := 0.818182 // buy
				if( VIP_VIM > -0.153564 )
					if( ema3 <= 183.926 )
						if( ema3 <= 182.804 )
							if( tema <= 153.749 )
								if( ema13 <= 0.083666 )
									ret := 0.577778
								if( ema13 > 0.083666 )
									ret := -0.069149
							if( tema > 153.749 )
								if( ema13 <= 0.374823 )
									ret := -0.189709
								if( ema13 > 0.374823 )
									ret := 0.066895
						if( ema3 > 182.804 )
							if( VIP_VIM <= 0.44514 )
								if( ema1 <= 183.538 )
									ret := 0.692308
								if( ema1 > 183.538 )
									ret := -0.180000
							if( VIP_VIM > 0.44514 )
								if( VIM <= 1.71833 )
									ret := 0.000000
								if( VIM > 1.71833 )
									ret := 0.789474 // buy
					if( ema3 > 183.926 )
						if( ema12 <= 0.050434 )
							if( ema1 <= 185.487 )
								if( ema1 <= 185.436 )
									ret := -0.289474
								if( ema1 > 185.436 )
									ret := -0.823529 // sell
							if( ema1 > 185.487 )
								if( VIP <= 1.80458 )
									ret := -0.464286
								if( VIP > 1.80458 )
									ret := 0.267857
						if( ema12 > 0.050434 )
							if( ema2 <= 191.025 )
								if( VIP_VIM <= 0.18368 )
									ret := -0.058824
								if( VIP_VIM > 0.18368 )
									ret := -0.776667 // sell
							if( ema2 > 191.025 )
								if( ema13 <= 0.216294 )
									ret := 0.272727
								if( ema13 > 0.216294 )
									ret := -0.928571 // sell
			if( VIP_VIM > 1.4658 )
				if( VIP <= 5.96061 )
					if( ema13 <= 0.263707 )
						if( ema2 <= 177.784 )
							if( ema2 <= 177.07 )
								if( tema <= 159.204 )
									ret := -0.730769 // sell
								if( tema > 159.204 )
									ret := -0.169492
							if( ema2 > 177.07 )
								if( ema12 <= 0.122844 )
									ret := -0.961538 // sell
								if( ema12 > 0.122844 )
									ret := -0.769231 // sell
						if( ema2 > 177.784 )
							if( tema <= 191.139 )
								if( ema2 <= 190.658 )
									ret := 0.044444
								if( ema2 > 190.658 )
									ret := 0.900000 // buy
							if( tema > 191.139 )
								ret := -0.615385
					if( ema13 > 0.263707 )
						if( VIM <= 0.728107 )
							ret := 1.000000 // buy
						if( VIM > 0.728107 )
							if( ema2 <= 156.407 )
								ret := 0.769231 // buy
							if( ema2 > 156.407 )
								if( VIP_VIM <= 1.73826 )
									ret := -0.222222
								if( VIP_VIM > 1.73826 )
									ret := 0.454545
				if( VIP > 5.96061 )
					if( VIP <= 26.4034 )
						if( ema2 <= 155.816 )
							ret := -0.400000
						if( ema2 > 155.816 )
							if( VIP <= 11.5833 )
								if( ema3 <= 164.389 )
									ret := 0.500000
								if( ema3 > 164.389 )
									ret := 0.083333
							if( VIP > 11.5833 )
								if( VIP <= 12.2281 )
									ret := 0.961538 // buy
								if( VIP > 12.2281 )
									ret := 0.452703
					if( VIP > 26.4034 )
						if( ema3 <= 178.696 )
							if( VIM <= 84.8222 )
								if( ema3 <= 164.917 )
									ret := -0.695652
								if( ema3 > 164.917 )
									ret := 0.281250
							if( VIM > 84.8222 )
								ret := 0.666667
						if( ema3 > 178.696 )
							if( ema13 <= 0.198079 )
								if( ema3 <= 181.4 )
									ret := -1.000000 // sell
								if( ema3 > 181.4 )
									ret := -0.769231 // sell
							if( ema13 > 0.198079 )
								ret := -0.625000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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
float op_operation = decision_tree_0_GOOG_1Min_08fb177b(ema12, ema3, ema13, tema, ema1, ema2, VIP, VIP_VIM, VIM)

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


