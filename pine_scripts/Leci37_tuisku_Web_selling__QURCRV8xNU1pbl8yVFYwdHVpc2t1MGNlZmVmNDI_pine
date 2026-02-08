//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA, L_Vortex_Indicator
// ID_model: ADBE_15Min_2TV0_0cefef42 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ADBE_15Min_2TV0_0cefef42", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ADBE_15Min_0cefef42(ema3, tema, ema2, ema12, ema13, ema1, VIP, VIM, VIP_VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( ema1 <= 515.279 )
		if( ema3 <= 515.592 )
			if( ema12 <= -0.122758 )
				if( VIP <= 0.928837 )
					if( tema <= 141.756 )
						if( tema <= 137.295 )
							if( ema12 <= -0.363387 )
								if( ema2 <= 135.485 )
									ret := -0.650794
								if( ema2 > 135.485 )
									ret := 0.363636
							if( ema12 > -0.363387 )
								if( tema <= 101.092 )
									ret := 0.764706 // buy
								if( tema > 101.092 )
									ret := -0.030172
						if( tema > 137.295 )
							if( VIM <= 1.18497 )
								if( ema2 <= 140.415 )
									ret := -1.000000 // sell
								if( ema2 > 140.415 )
									ret := 0.500000
							if( VIM > 1.18497 )
								if( ema2 <= 141.599 )
									ret := -0.682927
								if( ema2 > 141.599 )
									ret := -0.975000 // sell
					if( tema > 141.756 )
						if( ema12 <= -1.63904 )
							if( VIP_VIM <= -0.546483 )
								if( ema1 <= 249.788 )
									ret := -0.305085
								if( ema1 > 249.788 )
									ret := 0.110011
							if( VIP_VIM > -0.546483 )
								if( ema13 <= -2.69857 )
									ret := -0.179612
								if( ema13 > -2.69857 )
									ret := 0.244444
						if( ema12 > -1.63904 )
							if( ema1 <= 145.889 )
								if( VIM <= 1.24941 )
									ret := 0.190476
								if( VIM > 1.24941 )
									ret := 0.701754 // buy
							if( ema1 > 145.889 )
								if( ema2 <= 147.41 )
									ret := -0.633333
								if( ema2 > 147.41 )
									ret := 0.062999
				if( VIP > 0.928837 )
					if( ema3 <= 272.777 )
						if( VIP <= 1.04934 )
							if( ema13 <= -0.317901 )
								if( tema <= 269.23 )
									ret := 0.134783
								if( tema > 269.23 )
									ret := 0.638889
							if( ema13 > -0.317901 )
								if( ema3 <= 225.423 )
									ret := 0.057416
								if( ema3 > 225.423 )
									ret := -0.286585
						if( VIP > 1.04934 )
							if( ema12 <= -0.978676 )
								if( ema13 <= -2.61067 )
									ret := 0.806452 // buy
								if( ema13 > -2.61067 )
									ret := 0.445783
							if( ema12 > -0.978676 )
								if( VIP_VIM <= -0.701109 )
									ret := 0.633803
								if( VIP_VIM > -0.701109 )
									ret := 0.240143
					if( ema3 > 272.777 )
						if( ema1 <= 283.999 )
							if( VIM <= 1.76929 )
								if( ema2 <= 278.313 )
									ret := -0.034574
								if( ema2 > 278.313 )
									ret := -0.307054
							if( VIM > 1.76929 )
								if( ema3 <= 279.858 )
									ret := 0.613333
								if( ema3 > 279.858 )
									ret := -0.097561
						if( ema1 > 283.999 )
							if( ema1 <= 284.815 )
								if( ema3 <= 284.966 )
									ret := 0.000000
								if( ema3 > 284.966 )
									ret := 0.830769 // buy
							if( ema1 > 284.815 )
								if( ema3 <= 445.199 )
									ret := 0.139574
								if( ema3 > 445.199 )
									ret := 0.051993
			if( ema12 > -0.122758 )
				if( ema3 <= 511.65 )
					if( ema3 <= 103.543 )
						if( VIP <= 1.15833 )
							if( ema12 <= -0.025958 )
								if( VIP_VIM <= -0.044022 )
									ret := 0.037037
								if( VIP_VIM > -0.044022 )
									ret := 0.705882 // buy
							if( ema12 > -0.025958 )
								if( VIP_VIM <= 0.257682 )
									ret := -0.054545
								if( VIP_VIM > 0.257682 )
									ret := 0.500000
						if( VIP > 1.15833 )
							if( ema12 <= 0.294925 )
								if( ema1 <= 103.484 )
									ret := 0.814815 // buy
								if( ema1 > 103.484 )
									ret := 0.466667
							if( ema12 > 0.294925 )
								if( ema3 <= 103.274 )
									ret := 0.150000
								if( ema3 > 103.274 )
									ret := 1.000000 // buy
					if( ema3 > 103.543 )
						if( ema1 <= 245.842 )
							if( tema <= 233.243 )
								if( ema13 <= 1.35256 )
									ret := 0.031102
								if( ema13 > 1.35256 )
									ret := 0.245501
							if( tema > 233.243 )
								if( ema3 <= 234.924 )
									ret := 0.554688
								if( ema3 > 234.924 )
									ret := 0.172000
						if( ema1 > 245.842 )
							if( tema <= 256.968 )
								if( ema1 <= 246.504 )
									ret := -0.408696
								if( ema1 > 246.504 )
									ret := -0.061374
							if( tema > 256.968 )
								if( ema1 <= 257.821 )
									ret := 0.413793
								if( ema1 > 257.821 )
									ret := 0.027960
				if( ema3 > 511.65 )
					if( VIP <= 1.14774 )
						if( ema12 <= -0.048341 )
							if( tema <= 513.462 )
								ret := -0.142857
							if( tema > 513.462 )
								if( tema <= 514.695 )
									ret := 0.875000 // buy
								if( tema > 514.695 )
									ret := 0.000000
						if( ema12 > -0.048341 )
							if( VIM <= 1.02995 )
								if( ema1 <= 513.564 )
									ret := 0.625000
								if( ema1 > 513.564 )
									ret := -0.020833
							if( VIM > 1.02995 )
								if( ema2 <= 515.015 )
									ret := -0.233333
								if( ema2 > 515.015 )
									ret := -1.000000 // sell
					if( VIP > 1.14774 )
						if( VIM <= 0.908349 )
							if( ema12 <= 1.06233 )
								if( ema3 <= 514.416 )
									ret := -0.250000
								if( ema3 > 514.416 )
									ret := 0.125000
							if( ema12 > 1.06233 )
								if( ema1 <= 514.845 )
									ret := 1.000000 // buy
								if( ema1 > 514.845 )
									ret := 0.250000
						if( VIM > 0.908349 )
							if( ema13 <= 2.196 )
								if( ema12 <= 0.367205 )
									ret := 0.457143
								if( ema12 > 0.367205 )
									ret := 0.841584 // buy
							if( ema13 > 2.196 )
								if( VIP_VIM <= 0.333147 )
									ret := -0.857143 // sell
								if( VIP_VIM > 0.333147 )
									ret := 0.714286 // buy
		if( ema3 > 515.592 )
			if( ema1 <= 512.486 )
				if( ema3 <= 516.765 )
					if( VIP <= 0.953375 )
						if( ema1 <= 510.968 )
							ret := 0.000000
						if( ema1 > 510.968 )
							ret := 0.428571
					if( VIP > 0.953375 )
						ret := 1.000000 // buy
				if( ema3 > 516.765 )
					if( VIM <= 1.3521 )
						if( tema <= 508.117 )
							if( ema12 <= -6.28277 )
								ret := -1.000000 // sell
							if( ema12 > -6.28277 )
								ret := -0.250000
						if( tema > 508.117 )
							ret := -1.000000 // sell
					if( VIM > 1.3521 )
						if( ema1 <= 509.609 )
							if( ema3 <= 520.431 )
								ret := -0.500000
							if( ema3 > 520.431 )
								ret := -1.000000 // sell
						if( ema1 > 509.609 )
							if( VIP <= 0.74048 )
								ret := 0.250000
							if( VIP > 0.74048 )
								ret := 0.000000
			if( ema1 > 512.486 )
				if( ema3 <= 522.975 )
					if( tema <= 514.375 )
						if( ema12 <= -0.93354 )
							if( ema13 <= -1.43311 )
								if( VIP_VIM <= 0.19685 )
									ret := 0.654028
								if( VIP_VIM > 0.19685 )
									ret := -0.500000
							if( ema13 > -1.43311 )
								ret := -1.000000 // sell
						if( ema12 > -0.93354 )
							if( VIP <= 0.955423 )
								if( tema <= 513.548 )
									ret := 1.000000 // buy
								if( tema > 513.548 )
									ret := 0.200000
							if( VIP > 0.955423 )
								if( tema <= 513.388 )
									ret := 0.750000 // buy
								if( tema > 513.388 )
									ret := 1.000000 // buy
					if( tema > 514.375 )
						if( VIP <= 1.02861 )
							if( VIP <= 0.929178 )
								ret := -0.250000
							if( VIP > 0.929178 )
								ret := -1.000000 // sell
						if( VIP > 1.02861 )
							if( tema <= 515.685 )
								if( ema1 <= 514.946 )
									ret := -0.125000
								if( ema1 > 514.946 )
									ret := 0.642857
							if( tema > 515.685 )
								ret := 1.000000 // buy
				if( ema3 > 522.975 )
					ret := -0.500000
	if( ema1 > 515.279 )
		if( ema2 <= 527.149 )
			if( ema3 <= 523.452 )
				if( ema3 <= 519.603 )
					if( ema13 <= 2.87834 )
						if( ema3 <= 518.8 )
							if( ema3 <= 516.666 )
								if( ema3 <= 514.361 )
									ret := 0.165049
								if( ema3 > 514.361 )
									ret := -0.342466
							if( ema3 > 516.666 )
								if( VIM <= 0.943371 )
									ret := -0.443038
								if( VIM > 0.943371 )
									ret := 0.110032
						if( ema3 > 518.8 )
							if( ema2 <= 520.339 )
								if( ema2 <= 518.6 )
									ret := -0.075000
								if( ema2 > 518.6 )
									ret := -0.645833
							if( ema2 > 520.339 )
								if( tema <= 522.237 )
									ret := 0.400000
								if( tema > 522.237 )
									ret := 1.000000 // buy
					if( ema13 > 2.87834 )
						if( tema <= 527.269 )
							if( ema2 <= 520.62 )
								if( VIM <= 0.731313 )
									ret := 0.492063
								if( VIM > 0.731313 )
									ret := 0.019608
							if( ema2 > 520.62 )
								if( tema <= 524.244 )
									ret := 0.937500 // buy
								if( tema > 524.244 )
									ret := 0.411765
						if( tema > 527.269 )
							if( VIM <= 1.26419 )
								if( VIP_VIM <= 0.856805 )
									ret := -0.939394 // sell
								if( VIP_VIM > 0.856805 )
									ret := -0.333333
							if( VIM > 1.26419 )
								ret := 0.000000
				if( ema3 > 519.603 )
					if( VIM <= 1.27305 )
						if( VIP_VIM <= 0.281722 )
							if( ema2 <= 520.54 )
								if( ema1 <= 517.96 )
									ret := -0.175000
								if( ema1 > 517.96 )
									ret := 0.337079
							if( ema2 > 520.54 )
								if( ema3 <= 523.329 )
									ret := -0.305785
								if( ema3 > 523.329 )
									ret := 0.379310
						if( VIP_VIM > 0.281722 )
							if( tema <= 528.279 )
								if( ema13 <= 2.80094 )
									ret := 0.032258
								if( ema13 > 2.80094 )
									ret := 0.625000
							if( tema > 528.279 )
								if( tema <= 529.944 )
									ret := -0.607143
								if( tema > 529.944 )
									ret := 0.285714
					if( VIM > 1.27305 )
						if( ema1 <= 524.662 )
							if( ema12 <= -1.3515 )
								if( ema2 <= 520.709 )
									ret := 0.358974
								if( ema2 > 520.709 )
									ret := -0.521739
							if( ema12 > -1.3515 )
								if( ema3 <= 520.112 )
									ret := 0.187500
								if( ema3 > 520.112 )
									ret := 0.754902 // buy
						if( ema1 > 524.662 )
							ret := -1.000000 // sell
			if( ema3 > 523.452 )
				if( ema1 <= 526.398 )
					if( ema3 <= 526.125 )
						if( VIP <= 1.58996 )
							if( ema13 <= -2.33026 )
								if( VIP_VIM <= -0.810288 )
									ret := 0.166667
								if( VIP_VIM > -0.810288 )
									ret := -0.722892 // sell
							if( ema13 > -2.33026 )
								if( ema2 <= 524.021 )
									ret := 0.125000
								if( ema2 > 524.021 )
									ret := -0.372642
						if( VIP > 1.58996 )
							if( ema2 <= 523.903 )
								ret := 0.000000
							if( ema2 > 523.903 )
								if( ema2 <= 525.486 )
									ret := -0.733333 // sell
								if( ema2 > 525.486 )
									ret := -0.966667 // sell
					if( ema3 > 526.125 )
						if( VIP <= 1.45284 )
							if( tema <= 524.581 )
								if( VIM <= 1.51937 )
									ret := 0.152542
								if( VIM > 1.51937 )
									ret := -0.642857
							if( tema > 524.581 )
								if( VIM <= 1.37342 )
									ret := 0.133333
								if( VIM > 1.37342 )
									ret := 1.000000 // buy
						if( VIP > 1.45284 )
							if( VIP <= 2.30483 )
								if( VIP_VIM <= -0.157173 )
									ret := -0.944444 // sell
								if( VIP_VIM > -0.157173 )
									ret := 0.000000
							if( VIP > 2.30483 )
								ret := -0.142857
				if( ema1 > 526.398 )
					if( VIP_VIM <= 0.349017 )
						if( VIM <= 1.39713 )
							if( ema13 <= 0.673736 )
								if( ema3 <= 526.387 )
									ret := 0.823529 // buy
								if( ema3 > 526.387 )
									ret := -0.166667
							if( ema13 > 0.673736 )
								if( VIP <= 1.26232 )
									ret := -0.492754
								if( VIP > 1.26232 )
									ret := 0.375000
						if( VIM > 1.39713 )
							if( ema3 <= 525.723 )
								if( VIP_VIM <= 0.215917 )
									ret := -0.200000
								if( VIP_VIM > 0.215917 )
									ret := -0.750000 // sell
							if( ema3 > 525.723 )
								ret := -1.000000 // sell
					if( VIP_VIM > 0.349017 )
						if( VIP_VIM <= 0.735306 )
							if( VIP <= 1.36175 )
								if( ema12 <= 1.5718 )
									ret := 0.200000
								if( ema12 > 1.5718 )
									ret := -0.375000
							if( VIP > 1.36175 )
								if( ema12 <= 0.630167 )
									ret := 0.000000
								if( ema12 > 0.630167 )
									ret := 1.000000 // buy
						if( VIP_VIM > 0.735306 )
							if( ema13 <= 4.42096 )
								ret := 0.000000
							if( ema13 > 4.42096 )
								ret := -1.000000 // sell
		if( ema2 > 527.149 )
			if( ema1 <= 666.399 )
				if( ema12 <= 1.27216 )
					if( VIP_VIM <= -0.688004 )
						if( ema3 <= 647.781 )
							if( ema13 <= -8.17698 )
								if( VIP_VIM <= -0.925612 )
									ret := 0.016667
								if( VIP_VIM > -0.925612 )
									ret := -0.714286 // sell
							if( ema13 > -8.17698 )
								if( ema12 <= -1.42642 )
									ret := 0.242038
								if( ema12 > -1.42642 )
									ret := -0.345324
						if( ema3 > 647.781 )
							if( ema3 <= 666.499 )
								if( VIM <= 2.32333 )
									ret := -0.521739
								if( VIM > 2.32333 )
									ret := -0.942308 // sell
							if( ema3 > 666.499 )
								if( VIP_VIM <= -0.78613 )
									ret := 0.750000 // buy
								if( VIP_VIM > -0.78613 )
									ret := 0.142857
					if( VIP_VIM > -0.688004 )
						if( VIP <= 1.31113 )
							if( ema3 <= 530.418 )
								if( VIM <= 1.34516 )
									ret := 0.391892
								if( VIM > 1.34516 )
									ret := -0.111111
							if( ema3 > 530.418 )
								if( ema2 <= 530.391 )
									ret := -0.620690
								if( ema2 > 530.391 )
									ret := 0.035199
						if( VIP > 1.31113 )
							if( VIP_VIM <= 0.993058 )
								if( VIM <= 1.51254 )
									ret := 0.205351
								if( VIM > 1.51254 )
									ret := 0.057518
							if( VIP_VIM > 0.993058 )
								if( VIM <= 1.88438 )
									ret := 0.629630
								if( VIM > 1.88438 )
									ret := 1.000000 // buy
				if( ema12 > 1.27216 )
					if( ema12 <= 5.92328 )
						if( ema12 <= 1.82369 )
							if( ema2 <= 624.76 )
								if( VIP <= 1.54725 )
									ret := -0.149188
								if( VIP > 1.54725 )
									ret := -0.395833
							if( ema2 > 624.76 )
								if( ema13 <= 2.19348 )
									ret := 0.545455
								if( ema13 > 2.19348 )
									ret := 0.107692
						if( ema12 > 1.82369 )
							if( VIM <= 3.49733 )
								if( tema <= 665.777 )
									ret := 0.040000
								if( tema > 665.777 )
									ret := -0.567568
							if( VIM > 3.49733 )
								if( ema13 <= 4.83201 )
									ret := -0.500000
								if( ema13 > 4.83201 )
									ret := -1.000000 // sell
					if( ema12 > 5.92328 )
						if( VIP_VIM <= 0.412176 )
							ret := 0.000000
						if( VIP_VIM > 0.412176 )
							if( ema12 <= 6.54484 )
								ret := -1.000000 // sell
							if( ema12 > 6.54484 )
								if( VIM <= 1.12883 )
									ret := -0.500000
								if( VIM > 1.12883 )
									ret := -1.000000 // sell
			if( ema1 > 666.399 )
				if( VIM <= 3.07988 )
					if( VIP <= 0.971219 )
						if( ema1 <= 672.229 )
							if( ema2 <= 670.667 )
								if( VIP <= 0.918792 )
									ret := -0.125000
								if( VIP > 0.918792 )
									ret := 0.750000 // buy
							if( ema2 > 670.667 )
								if( VIP_VIM <= -0.412583 )
									ret := -0.545455
								if( VIP_VIM > -0.412583 )
									ret := -1.000000 // sell
						if( ema1 > 672.229 )
							if( ema3 <= 678.323 )
								if( VIP_VIM <= -0.209084 )
									ret := 1.000000 // buy
								if( VIP_VIM > -0.209084 )
									ret := -0.333333
							if( ema3 > 678.323 )
								if( ema2 <= 679.084 )
									ret := -0.722222 // sell
								if( ema2 > 679.084 )
									ret := 0.179487
					if( VIP > 0.971219 )
						if( ema3 <= 674.774 )
							if( ema2 <= 672.649 )
								if( VIP <= 2.2173 )
									ret := -0.398406
								if( VIP > 2.2173 )
									ret := 1.000000 // buy
							if( ema2 > 672.649 )
								if( ema12 <= 1.55301 )
									ret := 0.081081
								if( ema12 > 1.55301 )
									ret := 0.909091 // buy
						if( ema3 > 674.774 )
							if( VIM <= 0.867229 )
								if( ema1 <= 693.099 )
									ret := 0.090909
								if( ema1 > 693.099 )
									ret := -0.500000
							if( VIM > 0.867229 )
								if( tema <= 669.636 )
									ret := 0.200000
								if( tema > 669.636 )
									ret := -0.857143 // sell
				if( VIM > 3.07988 )
					if( VIP <= 5.85386 )
						ret := 1.000000 // buy
					if( VIP > 5.85386 )
						ret := 0.750000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_ADBE_15Min_0cefef42(ema3, tema, ema2, ema12, ema13, ema1, VIP, VIM, VIP_VIM)

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


