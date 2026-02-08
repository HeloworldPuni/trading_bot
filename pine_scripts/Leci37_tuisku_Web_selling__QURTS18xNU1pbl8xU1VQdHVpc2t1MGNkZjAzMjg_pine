//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: SuperTrend
// ID_model: ADSK_15Min_1SUP_0cdf0328 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ADSK_15Min_1SUP_0cdf0328", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ADSK_15Min_0cdf0328(atr, up, dn1, sellSignalInt, buySignalInt, atr2, dn, trend, up1)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( dn <= 199.401 )
		if( atr <= 0.510632 )
			if( up1 <= 83.594 )
				if( atr2 <= 0.348237 )
					if( dn1 <= 82.2358 )
						if( dn <= 81.4722 )
							if( atr <= 0.383065 )
								if( atr2 <= 0.16047 )
									ret := -0.288660
								if( atr2 > 0.16047 )
									ret := 0.022293
							if( atr > 0.383065 )
								if( up1 <= 73.5304 )
									ret := -1.000000 // sell
								if( up1 > 73.5304 )
									ret := 0.250000
						if( dn > 81.4722 )
							if( up1 <= 80.5923 )
								if( up1 <= 80.0351 )
									ret := -0.652174
								if( up1 > 80.0351 )
									ret := -0.094340
							if( up1 > 80.5923 )
								if( up1 <= 80.7902 )
									ret := -0.789474 // sell
								if( up1 > 80.7902 )
									ret := -0.441860
					if( dn1 > 82.2358 )
						if( dn <= 85.4545 )
							if( atr2 <= 0.1275 )
								ret := -1.000000 // sell
							if( atr2 > 0.1275 )
								if( atr2 <= 0.239101 )
									ret := 0.356481
								if( atr2 > 0.239101 )
									ret := 0.150442
						if( dn > 85.4545 )
							ret := -0.666667
				if( atr2 > 0.348237 )
					if( dn1 <= 77.7855 )
						if( dn1 <= 70.543 )
							if( up <= 67.6552 )
								ret := 1.000000 // buy
							if( up > 67.6552 )
								if( atr2 <= 0.424962 )
									ret := 0.750000 // buy
								if( atr2 > 0.424962 )
									ret := 0.800000 // buy
						if( dn1 > 70.543 )
							if( dn1 <= 73.8994 )
								if( up1 <= 70.771 )
									ret := 0.156250
								if( up1 > 70.771 )
									ret := -1.000000 // sell
							if( dn1 > 73.8994 )
								if( up1 <= 73.7251 )
									ret := 0.526316
								if( up1 > 73.7251 )
									ret := -0.333333
					if( dn1 > 77.7855 )
						if( up1 <= 77.1847 )
							if( atr <= 0.43639 )
								if( atr2 <= 0.503467 )
									ret := 0.527778
								if( atr2 > 0.503467 )
									ret := 1.000000 // buy
							if( atr > 0.43639 )
								if( atr <= 0.472124 )
									ret := 1.000000 // buy
								if( atr > 0.472124 )
									ret := 0.722222 // buy
						if( up1 > 77.1847 )
							if( up1 <= 82.072 )
								if( dn1 <= 84.6292 )
									ret := 0.185185
								if( dn1 > 84.6292 )
									ret := 0.708333 // buy
							if( up1 > 82.072 )
								if( dn <= 85.2118 )
									ret := 0.743590 // buy
								if( dn > 85.2118 )
									ret := 0.303030
			if( up1 > 83.594 )
				if( trend <= 0.99492 )
					if( dn <= 176.298 )
						if( dn1 <= 152.628 )
							if( dn <= 137.687 )
								if( sellSignalInt <= 0.5 )
									ret := 0.707317 // buy
								if( sellSignalInt > 0.5 )
									ret := 0.340426
							if( dn > 137.687 )
								if( atr2 <= 0.292945 )
									ret := 0.428571
								if( atr2 > 0.292945 )
									ret := -0.333333
						if( dn1 > 152.628 )
							if( up <= 158.385 )
								if( atr2 <= 0.314095 )
									ret := 0.857143 // buy
								if( atr2 > 0.314095 )
									ret := 1.000000 // buy
							if( up > 158.385 )
								if( up1 <= 161.013 )
									ret := 0.000000
								if( up1 > 161.013 )
									ret := 0.750000 // buy
					if( dn > 176.298 )
						if( atr <= 0.370551 )
							ret := -0.833333 // sell
						if( atr > 0.370551 )
							if( atr2 <= 0.436141 )
								ret := 0.750000 // buy
							if( atr2 > 0.436141 )
								ret := 0.250000
				if( trend > 0.99492 )
					if( dn1 <= 85.2799 )
						if( up <= 84.331 )
							if( dn1 <= 84.9024 )
								ret := -1.000000 // sell
							if( dn1 > 84.9024 )
								if( atr2 <= 0.228064 )
									ret := -0.153846
								if( atr2 > 0.228064 )
									ret := -0.928571 // sell
						if( up > 84.331 )
							ret := 0.600000
					if( dn1 > 85.2799 )
						if( atr2 <= 0.259389 )
							if( dn <= 171.68 )
								if( dn <= 153.96 )
									ret := 0.072471
								if( dn > 153.96 )
									ret := -0.383562
							if( dn > 171.68 )
								if( up <= 180.656 )
									ret := 0.843137 // buy
								if( up > 180.656 )
									ret := 0.140845
						if( atr2 > 0.259389 )
							if( dn1 <= 87.2933 )
								if( dn1 <= 86.1578 )
									ret := 0.025000
								if( dn1 > 86.1578 )
									ret := -0.274809
							if( dn1 > 87.2933 )
								if( up <= 85.5814 )
									ret := 0.423077
								if( up > 85.5814 )
									ret := 0.009044
		if( atr > 0.510632 )
			if( up1 <= 104.556 )
				if( dn <= 89.4148 )
					if( up1 <= 83.7994 )
						if( atr <= 0.538931 )
							if( atr2 <= 0.59156 )
								if( atr2 <= 0.420975 )
									ret := -0.400000
								if( atr2 > 0.420975 )
									ret := 0.771429 // buy
							if( atr2 > 0.59156 )
								if( up1 <= 80.9792 )
									ret := -0.600000
								if( up1 > 80.9792 )
									ret := 0.000000
						if( atr > 0.538931 )
							if( up1 <= 70.3428 )
								if( dn1 <= 73.4252 )
									ret := -0.166667
								if( dn1 > 73.4252 )
									ret := 0.777778 // buy
							if( up1 > 70.3428 )
								if( dn1 <= 78.3078 )
									ret := -0.451613
								if( dn1 > 78.3078 )
									ret := 0.051095
					if( up1 > 83.7994 )
						if( atr <= 0.770467 )
							if( atr <= 0.608667 )
								if( up <= 84.5943 )
									ret := 0.125000
								if( up > 84.5943 )
									ret := -0.666667
							if( atr > 0.608667 )
								if( up <= 84.2475 )
									ret := -0.750000 // sell
								if( up > 84.2475 )
									ret := -1.000000 // sell
						if( atr > 0.770467 )
							ret := 0.333333
				if( dn > 89.4148 )
					if( atr <= 1.1372 )
						if( dn1 <= 109.389 )
							if( dn1 <= 108.533 )
								if( up <= 99.1914 )
									ret := 0.600000
								if( up > 99.1914 )
									ret := 0.186047
							if( dn1 > 108.533 )
								if( atr2 <= 0.887877 )
									ret := -0.333333
								if( atr2 > 0.887877 )
									ret := 0.909091 // buy
						if( dn1 > 109.389 )
							if( atr <= 1.08267 )
								if( atr <= 1.05999 )
									ret := -0.360000
								if( atr > 1.05999 )
									ret := 1.000000 // buy
							if( atr > 1.08267 )
								ret := -1.000000 // sell
					if( atr > 1.1372 )
						if( dn1 <= 111.883 )
							if( dn <= 108.79 )
								if( dn <= 92.699 )
									ret := 0.600000
								if( dn > 92.699 )
									ret := 0.958333 // buy
							if( dn > 108.79 )
								if( up <= 104.02 )
									ret := 0.352941
								if( up > 104.02 )
									ret := 0.964286 // buy
						if( dn1 > 111.883 )
							if( atr2 <= 2.3735 )
								if( dn1 <= 112.668 )
									ret := -1.000000 // sell
								if( dn1 > 112.668 )
									ret := -0.111111
							if( atr2 > 2.3735 )
								ret := 0.571429
			if( up1 > 104.556 )
				if( up1 <= 191.551 )
					if( dn1 <= 195.293 )
						if( dn1 <= 177.639 )
							if( up <= 170.403 )
								if( up <= 169.228 )
									ret := 0.075791
								if( up > 169.228 )
									ret := 0.459459
							if( up > 170.403 )
								if( atr2 <= 0.632147 )
									ret := 0.024540
								if( atr2 > 0.632147 )
									ret := -0.353952
						if( dn1 > 177.639 )
							if( atr <= 2.10821 )
								if( up <= 174.841 )
									ret := 0.266082
								if( up > 174.841 )
									ret := 0.107471
							if( atr > 2.10821 )
								if( atr2 <= 2.4011 )
									ret := 0.661871
								if( atr2 > 2.4011 )
									ret := 0.214286
					if( dn1 > 195.293 )
						if( up1 <= 188.919 )
							if( atr <= 1.68363 )
								if( dn1 <= 197.558 )
									ret := -0.575000
								if( dn1 > 197.558 )
									ret := 0.000000
							if( atr > 1.68363 )
								if( atr <= 2.82033 )
									ret := 0.078788
								if( atr > 2.82033 )
									ret := -0.894737 // sell
						if( up1 > 188.919 )
							if( up <= 189.647 )
								if( atr <= 1.32753 )
									ret := 0.740000 // buy
								if( atr > 1.32753 )
									ret := 0.117647
							if( up > 189.647 )
								if( dn <= 199.035 )
									ret := 0.005111
								if( dn > 199.035 )
									ret := 0.694444
				if( up1 > 191.551 )
					if( up1 <= 193.347 )
						if( atr2 <= 0.6984 )
							if( up <= 192.79 )
								if( dn1 <= 196.559 )
									ret := 0.573770
								if( dn1 > 196.559 )
									ret := 0.857143 // buy
							if( up > 192.79 )
								if( up1 <= 192.663 )
									ret := -0.400000
								if( up1 > 192.663 )
									ret := 0.422680
						if( atr2 > 0.6984 )
							if( dn1 <= 196.754 )
								if( dn <= 196.665 )
									ret := -0.090909
								if( dn > 196.665 )
									ret := -0.571429
							if( dn1 > 196.754 )
								if( atr2 <= 0.995419 )
									ret := 0.357401
								if( atr2 > 0.995419 )
									ret := 0.097561
					if( up1 > 193.347 )
						if( dn1 <= 197.107 )
							if( dn <= 196.857 )
								if( dn <= 196.399 )
									ret := -0.764706 // sell
								if( dn > 196.399 )
									ret := 0.187500
							if( dn > 196.857 )
								if( dn <= 196.95 )
									ret := -0.750000 // sell
								if( dn > 196.95 )
									ret := -1.000000 // sell
						if( dn1 > 197.107 )
							if( atr2 <= 0.54052 )
								if( atr <= 0.626784 )
									ret := 0.492537
								if( atr > 0.626784 )
									ret := -0.750000 // sell
							if( atr2 > 0.54052 )
								if( atr2 <= 0.794227 )
									ret := -0.023599
								if( atr2 > 0.794227 )
									ret := 0.290123
	if( dn > 199.401 )
		if( trend <= 0.962649 )
			if( up <= 197.693 )
				if( atr <= 0.983178 )
					ret := -0.500000
				if( atr > 0.983178 )
					ret := -1.000000 // sell
			if( up > 197.693 )
				if( atr <= 1.52781 )
					if( dn <= 204.043 )
						if( atr <= 0.861412 )
							ret := 1.000000 // buy
						if( atr > 0.861412 )
							if( dn1 <= 202.846 )
								if( dn1 <= 202.123 )
									ret := 0.750000 // buy
								if( dn1 > 202.123 )
									ret := 1.000000 // buy
							if( dn1 > 202.846 )
								ret := 0.400000
					if( dn > 204.043 )
						if( atr2 <= 0.602336 )
							if( trend <= 0.15103 )
								if( trend <= -0.533369 )
									ret := 0.035714
								if( trend > -0.533369 )
									ret := -0.800000 // sell
							if( trend > 0.15103 )
								if( dn <= 243.35 )
									ret := 0.333333
								if( dn > 243.35 )
									ret := 1.000000 // buy
						if( atr2 > 0.602336 )
							if( atr <= 0.877019 )
								if( dn <= 300.979 )
									ret := 0.794872 // buy
								if( dn > 300.979 )
									ret := -0.142857
							if( atr > 0.877019 )
								if( atr <= 0.909834 )
									ret := -0.230769
								if( atr > 0.909834 )
									ret := 0.389313
				if( atr > 1.52781 )
					if( dn <= 211.203 )
						if( atr <= 1.87541 )
							if( up <= 201.46 )
								if( atr2 <= 1.17864 )
									ret := 0.750000 // buy
								if( atr2 > 1.17864 )
									ret := -0.600000
							if( up > 201.46 )
								ret := 1.000000 // buy
						if( atr > 1.87541 )
							ret := 1.000000 // buy
					if( dn > 211.203 )
						if( up <= 218.739 )
							if( atr2 <= 1.28817 )
								ret := 0.000000
							if( atr2 > 1.28817 )
								if( dn1 <= 221.33 )
									ret := -0.750000 // sell
								if( dn1 > 221.33 )
									ret := -1.000000 // sell
						if( up > 218.739 )
							if( atr2 <= 1.49284 )
								if( dn1 <= 236.696 )
									ret := 0.538462
								if( dn1 > 236.696 )
									ret := -0.439024
							if( atr2 > 1.49284 )
								if( dn1 <= 277.621 )
									ret := 0.027027
								if( dn1 > 277.621 )
									ret := 0.704545 // buy
		if( trend > 0.962649 )
			if( atr2 <= 1.84255 )
				if( dn <= 224.385 )
					if( atr <= 1.12606 )
						if( dn <= 219.485 )
							if( dn1 <= 217.027 )
								if( up <= 211.031 )
									ret := 0.025968
								if( up > 211.031 )
									ret := -0.150459
							if( dn1 > 217.027 )
								if( up1 <= 213.904 )
									ret := 0.332103
								if( up1 > 213.904 )
									ret := -0.039337
						if( dn > 219.485 )
							if( up1 <= 214.506 )
								if( up <= 213.41 )
									ret := 0.750000 // buy
								if( up > 213.41 )
									ret := -0.585859
							if( up1 > 214.506 )
								if( dn <= 223.472 )
									ret := -0.009756
								if( dn > 223.472 )
									ret := -0.292208
					if( atr > 1.12606 )
						if( up1 <= 196.75 )
							if( up1 <= 188.911 )
								ret := -1.000000 // sell
							if( up1 > 188.911 )
								if( up <= 197.425 )
									ret := 0.048035
								if( up > 197.425 )
									ret := 0.863636 // buy
						if( up1 > 196.75 )
							if( dn <= 205.172 )
								if( dn1 <= 203.134 )
									ret := 0.461538
								if( dn1 > 203.134 )
									ret := -0.635514
							if( dn > 205.172 )
								if( atr2 <= 1.78038 )
									ret := -0.115473
								if( atr2 > 1.78038 )
									ret := 0.296610
				if( dn > 224.385 )
					if( up1 <= 228.729 )
						if( atr2 <= 1.38402 )
							if( up <= 220.068 )
								if( dn1 <= 225.743 )
									ret := 0.060241
								if( dn1 > 225.743 )
									ret := -0.442857
							if( up > 220.068 )
								if( atr2 <= 0.463894 )
									ret := 0.575000
								if( atr2 > 0.463894 )
									ret := 0.141791
						if( atr2 > 1.38402 )
							if( up1 <= 217.811 )
								if( dn1 <= 225.076 )
									ret := 0.000000
								if( dn1 > 225.076 )
									ret := 0.792453 // buy
							if( up1 > 217.811 )
								if( up <= 219.381 )
									ret := -0.260870
								if( up > 219.381 )
									ret := 0.292982
					if( up1 > 228.729 )
						if( dn1 <= 233.751 )
							if( atr2 <= 0.504 )
								ret := 0.000000
							if( atr2 > 0.504 )
								if( dn1 <= 233.111 )
									ret := -0.333333
								if( dn1 > 233.111 )
									ret := -0.920000 // sell
						if( dn1 > 233.751 )
							if( dn1 <= 293.661 )
								if( dn <= 286.804 )
									ret := 0.032172
								if( dn > 286.804 )
									ret := 0.156194
							if( dn1 > 293.661 )
								if( atr2 <= 0.567165 )
									ret := 0.183168
								if( atr2 > 0.567165 )
									ret := -0.046702
			if( atr2 > 1.84255 )
				if( up <= 187.873 )
					if( dn1 <= 203.011 )
						if( up1 <= 184.554 )
							ret := 0.250000
						if( up1 > 184.554 )
							if( atr <= 2.23607 )
								ret := 0.750000 // buy
							if( atr > 2.23607 )
								ret := 1.000000 // buy
					if( dn1 > 203.011 )
						ret := 0.000000
				if( up > 187.873 )
					if( dn <= 207.758 )
						if( up <= 192.136 )
							if( dn <= 203.207 )
								if( atr <= 2.19398 )
									ret := -0.524590
								if( atr > 2.19398 )
									ret := 0.294118
							if( dn > 203.207 )
								if( dn1 <= 203.607 )
									ret := -0.875000 // sell
								if( dn1 > 203.607 )
									ret := 0.230769
						if( up > 192.136 )
							if( atr <= 1.8837 )
								if( atr <= 1.50229 )
									ret := -0.882353 // sell
								if( atr > 1.50229 )
									ret := -0.294118
							if( atr > 1.8837 )
								if( up1 <= 191.165 )
									ret := -0.300000
								if( up1 > 191.165 )
									ret := -0.820000 // sell
					if( dn > 207.758 )
						if( up <= 202.188 )
							if( up1 <= 190.907 )
								ret := -0.714286 // sell
							if( up1 > 190.907 )
								if( dn <= 211.409 )
									ret := 0.640000
								if( dn > 211.409 )
									ret := 0.300000
						if( up > 202.188 )
							if( up <= 204.619 )
								if( atr <= 2.56744 )
									ret := -0.647059
								if( atr > 2.56744 )
									ret := 0.625000
							if( up > 204.619 )
								if( up <= 296.793 )
									ret := -0.063771
								if( up > 296.793 )
									ret := 0.165957
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator SuperTrend 
//@version=5
//indicator title="Supertrend", overlay=true, format=format.price, precision=2, timeframe="")

Periods = input.int(title="ATR Period", defval=10)
src = input.source(hl2, title="Source")
Multiplier = input.float(title="ATR Multiplier", step=0.1, defval=3.0)
changeATR = input.bool(title="Change ATR Calculation Method?", defval=true)
showsignals = input.bool(title="Show Buy/Sell Signals?", defval=true)
highlighting = input.bool(title="Highlighter On/Off?", defval=true)

atr2 = ta.sma(ta.tr, Periods)
atr = changeATR ? ta.atr(Periods) : atr2

up = src - (Multiplier * atr)
up1 = nz(up[1], up)
up := close[1] > up1 ? math.max(up, up1) : up

dn = src + (Multiplier * atr)
dn1 = nz(dn[1], dn)
dn := close[1] < dn1 ? math.min(dn, dn1) : dn

var trend = 1
trend := nz(trend[1], trend)
trend := trend == -1 and close > dn1 ? 1 : trend == 1 and close < up1 ? -1 : trend

upPlot = plot(trend == 1 ? up : na, title="Up Trend", style=plot.style_linebr, linewidth=2, color=color.green)
dnPlot = plot(trend == 1 ? na : dn, title="Down Trend", style=plot.style_linebr, linewidth=2, color=color.red)

buySignal = trend == 1 and trend[1] == -1
sellSignal = trend == -1 and trend[1] == 1

plotshape(buySignal, title="UpTrend Begins", location=location.absolute, style=shape.circle, size=size.tiny, color=color.green, textcolor=color.white)
plotshape(sellSignal, title="DownTrend Begins", location=location.absolute, style=shape.circle, size=size.tiny, color=color.red, textcolor=color.white)

plotshape(showsignals and buySignal, title="Buy", text="Buy", location=location.absolute, style=shape.labelup, size=size.tiny, color=color.green, textcolor=color.white)
plotshape(showsignals and sellSignal, title="Sell", text="Sell", location=location.absolute, style=shape.labeldown, size=size.tiny, color=color.red, textcolor=color.white)

mPlot = plot(ohlc4, title="", style=plot.style_circles, linewidth=1)

longFillColor = highlighting ? (trend == 1 ? color.new(color.green, 80) : color.new(color.white, 100)) : color.new(color.white, 100)
shortFillColor = highlighting ? (trend == -1 ? color.new(color.red, 80) : color.new(color.white, 100)) : color.new(color.white, 100)

fill(mPlot, upPlot, title="UpTrend Highlighter", color=longFillColor)
fill(mPlot, dnPlot, title="DownTrend Highlighter", color=shortFillColor)

alertcondition(buySignal, title="SuperTrend Buy", message="SuperTrend Buy!")
alertcondition(sellSignal, title="SuperTrend Sell", message="SuperTrend Sell!")
changeCond = trend != trend[1]
alertcondition(changeCond, title="SuperTrend Direction Change", message="SuperTrend has changed direction!")

buySignalInt = buySignal ? 1: 0   //Bool to int
sellSignalInt = sellSignal ? 1: 0   //Bool to int

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
float op_operation = decision_tree_0_ADSK_15Min_0cdf0328(atr, up, dn1, sellSignalInt, buySignalInt, atr2, dn, trend, up1)

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


