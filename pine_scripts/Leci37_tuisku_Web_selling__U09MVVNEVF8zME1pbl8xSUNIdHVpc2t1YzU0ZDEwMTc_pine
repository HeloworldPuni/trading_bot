//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Ichimoku_Cloud
// ID_model: SOLUSDT_30Min_1ICH_c54d1017 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SOLUSDT_30Min_1ICH_c54d1017", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SOLUSDT_30Min_c54d1017(tenkan_sen, basis_minus, cross_up_tenkan_kinjunInt, senkou_span_a, cross_dn_tenkan_kinjunInt, senkou_span_b, chinkou_span, senkou_span_a_displaced, senkou_span_b_displaced, kinjun_sen, basis_max)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( senkou_span_a_displaced <= 13.5265 )
		if( chinkou_span <= 13.6242 )
			if( senkou_span_a <= 1.34603 )
				if( senkou_span_b <= 1.39037 )
					if( basis_minus <= -0.027427 )
						if( basis_max <= 0.00762 )
							if( kinjun_sen <= 1.18696 )
								ret := 0.500000
							if( kinjun_sen > 1.18696 )
								ret := 1.000000 // buy
						if( basis_max > 0.00762 )
							if( basis_minus <= -0.036037 )
								if( senkou_span_a <= 1.18805 )
									ret := 0.666667
								if( senkou_span_a > 1.18805 )
									ret := 0.937500 // buy
							if( basis_minus > -0.036037 )
								ret := 0.000000
					if( basis_minus > -0.027427 )
						if( chinkou_span <= 1.32503 )
							if( senkou_span_b <= 1.29968 )
								ret := 0.500000
							if( senkou_span_b > 1.29968 )
								if( tenkan_sen <= 1.33364 )
									ret := -1.000000 // sell
								if( tenkan_sen > 1.33364 )
									ret := -0.750000 // sell
						if( chinkou_span > 1.32503 )
							if( kinjun_sen <= 1.16817 )
								ret := -0.500000
							if( kinjun_sen > 1.16817 )
								if( senkou_span_a_displaced <= 1.36772 )
									ret := 0.601852
								if( senkou_span_a_displaced > 1.36772 )
									ret := 0.000000
				if( senkou_span_b > 1.39037 )
					if( basis_minus <= -0.087096 )
						ret := -1.000000 // sell
					if( basis_minus > -0.087096 )
						ret := -0.750000 // sell
			if( senkou_span_a > 1.34603 )
				if( chinkou_span <= 1.48301 )
					if( tenkan_sen <= 1.52048 )
						if( senkou_span_b_displaced <= 1.35569 )
							if( tenkan_sen <= 1.39027 )
								if( senkou_span_a_displaced <= 1.3312 )
									ret := 0.500000
								if( senkou_span_a_displaced > 1.3312 )
									ret := 1.000000 // buy
							if( tenkan_sen > 1.39027 )
								if( basis_max <= -0.012363 )
									ret := 0.227273
								if( basis_max > -0.012363 )
									ret := -0.521739
						if( senkou_span_b_displaced > 1.35569 )
							if( tenkan_sen <= 1.36655 )
								if( senkou_span_a_displaced <= 1.51839 )
									ret := 0.267857
								if( senkou_span_a_displaced > 1.51839 )
									ret := -1.000000 // sell
							if( tenkan_sen > 1.36655 )
								if( chinkou_span <= 1.41995 )
									ret := -0.551724
								if( chinkou_span > 1.41995 )
									ret := 0.017544
					if( tenkan_sen > 1.52048 )
						if( basis_max <= -0.010075 )
							if( basis_minus <= 0.010287 )
								ret := -0.250000
							if( basis_minus > 0.010287 )
								ret := 0.166667
						if( basis_max > -0.010075 )
							if( senkou_span_a <= 1.60646 )
								if( basis_max <= 0.010788 )
									ret := -0.923077 // sell
								if( basis_max > 0.010788 )
									ret := -0.285714
							if( senkou_span_a > 1.60646 )
								ret := -0.200000
				if( chinkou_span > 1.48301 )
					if( senkou_span_b_displaced <= 1.53356 )
						if( basis_minus <= 0.06817 )
							if( basis_minus <= 0.0127 )
								if( senkou_span_b_displaced <= 1.48569 )
									ret := 0.536585
								if( senkou_span_b_displaced > 1.48569 )
									ret := 0.880597 // buy
							if( basis_minus > 0.0127 )
								if( basis_minus <= 0.019438 )
									ret := -0.028986
								if( basis_minus > 0.019438 )
									ret := 0.402516
						if( basis_minus > 0.06817 )
							if( senkou_span_b <= 1.65972 )
								if( chinkou_span <= 2.1962 )
									ret := 0.804878 // buy
								if( chinkou_span > 2.1962 )
									ret := 1.000000 // buy
							if( senkou_span_b > 1.65972 )
								if( chinkou_span <= 2.13521 )
									ret := -0.428571
								if( chinkou_span > 2.13521 )
									ret := 1.000000 // buy
					if( senkou_span_b_displaced > 1.53356 )
						if( chinkou_span <= 3.31616 )
							if( senkou_span_a <= 2.90751 )
								if( basis_max <= 0.020501 )
									ret := 0.034591
								if( basis_max > 0.020501 )
									ret := 0.312217
							if( senkou_span_a > 2.90751 )
								if( tenkan_sen <= 3.34573 )
									ret := -0.135674
								if( tenkan_sen > 3.34573 )
									ret := -0.543478
						if( chinkou_span > 3.31616 )
							if( senkou_span_a <= 3.18667 )
								if( senkou_span_a <= 2.42101 )
									ret := -0.444444
								if( senkou_span_a > 2.42101 )
									ret := 0.831933 // buy
							if( senkou_span_a > 3.18667 )
								if( senkou_span_b_displaced <= 8.88004 )
									ret := 0.209219
								if( senkou_span_b_displaced > 8.88004 )
									ret := -0.013348
		if( chinkou_span > 13.6242 )
			if( senkou_span_a_displaced <= 10.6866 )
				if( kinjun_sen <= 12.1721 )
					ret := -0.500000
				if( kinjun_sen > 12.1721 )
					ret := -1.000000 // sell
			if( senkou_span_a_displaced > 10.6866 )
				if( tenkan_sen <= 13.2096 )
					if( senkou_span_a_displaced <= 13.25 )
						if( basis_max <= -0.144912 )
							if( senkou_span_b <= 12.2178 )
								if( senkou_span_a_displaced <= 11.6951 )
									ret := 0.950000 // buy
								if( senkou_span_a_displaced > 11.6951 )
									ret := 0.333333
							if( senkou_span_b > 12.2178 )
								if( basis_minus <= 0.219924 )
									ret := 0.666667
								if( basis_minus > 0.219924 )
									ret := -0.437500
						if( basis_max > -0.144912 )
							if( senkou_span_a_displaced <= 13.0746 )
								if( chinkou_span <= 14.5414 )
									ret := 0.965035 // buy
								if( chinkou_span > 14.5414 )
									ret := 0.822222 // buy
							if( senkou_span_a_displaced > 13.0746 )
								if( senkou_span_b <= 13.1134 )
									ret := 0.892857 // buy
								if( senkou_span_b > 13.1134 )
									ret := -0.400000
					if( senkou_span_a_displaced > 13.25 )
						if( kinjun_sen <= 12.8706 )
							ret := -1.000000 // sell
						if( kinjun_sen > 12.8706 )
							if( basis_max <= -0.008273 )
								ret := 0.250000
							if( basis_max > -0.008273 )
								ret := 0.200000
				if( tenkan_sen > 13.2096 )
					if( chinkou_span <= 14.4885 )
						if( senkou_span_b_displaced <= 13.2319 )
							if( tenkan_sen <= 13.645 )
								if( chinkou_span <= 13.7637 )
									ret := -0.500000
								if( chinkou_span > 13.7637 )
									ret := -1.000000 // sell
							if( tenkan_sen > 13.645 )
								if( senkou_span_b <= 13.4676 )
									ret := 0.142857
								if( senkou_span_b > 13.4676 )
									ret := -0.761905 // sell
						if( senkou_span_b_displaced > 13.2319 )
							if( tenkan_sen <= 14.4179 )
								if( kinjun_sen <= 13.1725 )
									ret := 1.000000 // buy
								if( kinjun_sen > 13.1725 )
									ret := 0.185185
							if( tenkan_sen > 14.4179 )
								ret := -1.000000 // sell
					if( chinkou_span > 14.4885 )
						if( basis_minus <= 1.3362 )
							if( basis_max <= -0.589988 )
								if( senkou_span_a_displaced <= 13.3908 )
									ret := -0.500000
								if( senkou_span_a_displaced > 13.3908 )
									ret := 1.000000 // buy
							if( basis_max > -0.589988 )
								if( senkou_span_a_displaced <= 13.3981 )
									ret := 0.634021
								if( senkou_span_a_displaced > 13.3981 )
									ret := 0.934426 // buy
						if( basis_minus > 1.3362 )
							if( basis_max <= -0.321951 )
								ret := -1.000000 // sell
							if( basis_max > -0.321951 )
								if( senkou_span_b <= 12.506 )
									ret := 0.750000 // buy
								if( senkou_span_b > 12.506 )
									ret := -0.250000
	if( senkou_span_a_displaced > 13.5265 )
		if( chinkou_span <= 13.3021 )
			if( basis_max <= 0.161325 )
				if( chinkou_span <= 12.6132 )
					if( basis_minus <= -0.486413 )
						if( tenkan_sen <= 13.6095 )
							if( basis_max <= 0.115281 )
								ret := 0.000000
							if( basis_max > 0.115281 )
								ret := 0.250000
						if( tenkan_sen > 13.6095 )
							ret := -0.714286 // sell
					if( basis_minus > -0.486413 )
						if( senkou_span_a <= 12.6633 )
							ret := -0.333333
						if( senkou_span_a > 12.6633 )
							if( basis_max <= 0.024462 )
								ret := -0.333333
							if( basis_max > 0.024462 )
								if( chinkou_span <= 11.7716 )
									ret := -0.400000
								if( chinkou_span > 11.7716 )
									ret := -0.917526 // sell
				if( chinkou_span > 12.6132 )
					if( basis_minus <= -0.713929 )
						ret := 0.833333 // buy
					if( basis_minus > -0.713929 )
						if( basis_minus <= -0.082769 )
							if( senkou_span_b_displaced <= 13.014 )
								if( senkou_span_a_displaced <= 13.7793 )
									ret := -0.750000 // sell
								if( senkou_span_a_displaced > 13.7793 )
									ret := -1.000000 // sell
							if( senkou_span_b_displaced > 13.014 )
								if( chinkou_span <= 12.8057 )
									ret := -0.482759
								if( chinkou_span > 12.8057 )
									ret := -0.118644
						if( basis_minus > -0.082769 )
							if( tenkan_sen <= 13.5576 )
								if( senkou_span_a_displaced <= 13.6433 )
									ret := -1.000000 // sell
								if( senkou_span_a_displaced > 13.6433 )
									ret := -0.500000
							if( tenkan_sen > 13.5576 )
								if( senkou_span_a <= 13.8365 )
									ret := -0.346939
								if( senkou_span_a > 13.8365 )
									ret := -0.794872 // sell
			if( basis_max > 0.161325 )
				if( senkou_span_a <= 14.0529 )
					if( senkou_span_b <= 14.1554 )
						if( senkou_span_b_displaced <= 14.49 )
							if( senkou_span_b_displaced <= 14.09 )
								if( senkou_span_b_displaced <= 14.0306 )
									ret := 0.000000
								if( senkou_span_b_displaced > 14.0306 )
									ret := -1.000000 // sell
							if( senkou_span_b_displaced > 14.09 )
								if( basis_minus <= -0.411076 )
									ret := 0.600000
								if( basis_minus > -0.411076 )
									ret := 0.000000
						if( senkou_span_b_displaced > 14.49 )
							if( basis_max <= 0.331875 )
								ret := -0.250000
							if( basis_max > 0.331875 )
								ret := -1.000000 // sell
					if( senkou_span_b > 14.1554 )
						if( senkou_span_b_displaced <= 14.4373 )
							if( chinkou_span <= 13.1847 )
								ret := 1.000000 // buy
							if( chinkou_span > 13.1847 )
								ret := 0.750000 // buy
						if( senkou_span_b_displaced > 14.4373 )
							if( basis_minus <= -0.559195 )
								ret := 1.000000 // buy
							if( basis_minus > -0.559195 )
								ret := -0.500000
				if( senkou_span_a > 14.0529 )
					ret := -1.000000 // sell
		if( chinkou_span > 13.3021 )
			if( tenkan_sen <= 138.827 )
				if( chinkou_span <= 137.881 )
					if( basis_max <= -0.828456 )
						if( chinkou_span <= 108.197 )
							if( senkou_span_b_displaced <= 106.23 )
								if( senkou_span_b_displaced <= 93.7107 )
									ret := 0.142857
								if( senkou_span_b_displaced > 93.7107 )
									ret := -0.284644
							if( senkou_span_b_displaced > 106.23 )
								if( basis_max <= -1.31375 )
									ret := 0.250000
								if( basis_max > -1.31375 )
									ret := 0.913043 // buy
						if( chinkou_span > 108.197 )
							if( basis_minus <= 7.05 )
								if( senkou_span_b_displaced <= 111.341 )
									ret := 0.527363
								if( senkou_span_b_displaced > 111.341 )
									ret := 0.232558
							if( basis_minus > 7.05 )
								if( senkou_span_a <= 124.964 )
									ret := -0.875000 // sell
								if( senkou_span_a > 124.964 )
									ret := -0.470588
					if( basis_max > -0.828456 )
						if( kinjun_sen <= 132.658 )
							if( chinkou_span <= 132.742 )
								if( kinjun_sen <= 115.182 )
									ret := 0.040124
								if( kinjun_sen > 115.182 )
									ret := -0.163366
							if( chinkou_span > 132.742 )
								if( basis_minus <= 6.05099 )
									ret := 0.474801
								if( basis_minus > 6.05099 )
									ret := -0.900000 // sell
						if( kinjun_sen > 132.658 )
							if( kinjun_sen <= 133.224 )
								if( senkou_span_a <= 133.406 )
									ret := -0.225000
								if( senkou_span_a > 133.406 )
									ret := -0.893617 // sell
							if( kinjun_sen > 133.224 )
								if( basis_max <= -0.183821 )
									ret := 0.161290
								if( basis_max > -0.183821 )
									ret := -0.176829
				if( chinkou_span > 137.881 )
					if( senkou_span_a <= 132.733 )
						if( kinjun_sen <= 128.695 )
							if( basis_minus <= -0.81375 )
								if( senkou_span_b_displaced <= 135.416 )
									ret := -0.454545
								if( senkou_span_b_displaced > 135.416 )
									ret := 0.772727 // buy
							if( basis_minus > -0.81375 )
								if( senkou_span_a <= 129.768 )
									ret := 0.768293 // buy
								if( senkou_span_a > 129.768 )
									ret := 0.200000
						if( kinjun_sen > 128.695 )
							if( kinjun_sen <= 134.632 )
								if( tenkan_sen <= 133.912 )
									ret := 0.886486 // buy
								if( tenkan_sen > 133.912 )
									ret := 0.250000
							if( kinjun_sen > 134.632 )
								ret := -0.200000
					if( senkou_span_a > 132.733 )
						if( chinkou_span <= 144.326 )
							if( tenkan_sen <= 133.146 )
								if( chinkou_span <= 138.704 )
									ret := -0.500000
								if( chinkou_span > 138.704 )
									ret := 0.916667 // buy
							if( tenkan_sen > 133.146 )
								if( senkou_span_a_displaced <= 141.198 )
									ret := 0.135729
								if( senkou_span_a_displaced > 141.198 )
									ret := 0.432432
						if( chinkou_span > 144.326 )
							if( basis_max <= -1.30601 )
								if( tenkan_sen <= 137.754 )
									ret := -0.800000 // sell
								if( tenkan_sen > 137.754 )
									ret := 0.333333
							if( basis_max > -1.30601 )
								if( senkou_span_b <= 130.842 )
									ret := 0.981481 // buy
								if( senkou_span_b > 130.842 )
									ret := 0.733871 // buy
			if( tenkan_sen > 138.827 )
				if( kinjun_sen <= 139.434 )
					if( chinkou_span <= 139.265 )
						if( tenkan_sen <= 140.44 )
							if( kinjun_sen <= 138.59 )
								if( basis_max <= -2.39606 )
									ret := -1.000000 // sell
								if( basis_max > -2.39606 )
									ret := -0.438596
							if( kinjun_sen > 138.59 )
								if( senkou_span_a_displaced <= 141.147 )
									ret := -0.854839 // sell
								if( senkou_span_a_displaced > 141.147 )
									ret := -0.166667
						if( tenkan_sen > 140.44 )
							if( basis_minus <= 1.6473 )
								ret := -1.000000 // sell
							if( basis_minus > 1.6473 )
								if( basis_minus <= 2.4975 )
									ret := -0.500000
								if( basis_minus > 2.4975 )
									ret := -1.000000 // sell
					if( chinkou_span > 139.265 )
						if( basis_max <= -2.14808 )
							if( basis_minus <= 4.0075 )
								if( senkou_span_b_displaced <= 140.705 )
									ret := 0.000000
								if( senkou_span_b_displaced > 140.705 )
									ret := -0.750000 // sell
							if( basis_minus > 4.0075 )
								if( kinjun_sen <= 137.698 )
									ret := -0.926829 // sell
								if( kinjun_sen > 137.698 )
									ret := -0.500000
						if( basis_max > -2.14808 )
							if( senkou_span_b <= 134.898 )
								if( senkou_span_b_displaced <= 132.812 )
									ret := 0.536082
								if( senkou_span_b_displaced > 132.812 )
									ret := -0.571429
							if( senkou_span_b > 134.898 )
								if( senkou_span_b_displaced <= 143.615 )
									ret := -0.125874
								if( senkou_span_b_displaced > 143.615 )
									ret := -0.793103 // sell
				if( kinjun_sen > 139.434 )
					if( chinkou_span <= 144.984 )
						if( kinjun_sen <= 147.713 )
							if( basis_max <= -0.010188 )
								if( basis_max <= -2.305 )
									ret := 0.833333 // buy
								if( basis_max > -2.305 )
									ret := -0.322619
							if( basis_max > -0.010188 )
								if( senkou_span_b_displaced <= 135.908 )
									ret := -0.781250 // sell
								if( senkou_span_b_displaced > 135.908 )
									ret := 0.002830
						if( kinjun_sen > 147.713 )
							if( kinjun_sen <= 150.982 )
								if( basis_minus <= -6.88581 )
									ret := 0.736842 // buy
								if( basis_minus > -6.88581 )
									ret := -0.504323
							if( kinjun_sen > 150.982 )
								if( basis_max <= 0.18999 )
									ret := -0.833333 // sell
								if( basis_max > 0.18999 )
									ret := -0.620155
					if( chinkou_span > 144.984 )
						if( kinjun_sen <= 150.478 )
							if( tenkan_sen <= 142.767 )
								if( basis_max <= -0.16228 )
									ret := 0.176000
								if( basis_max > -0.16228 )
									ret := 0.648221
							if( tenkan_sen > 142.767 )
								if( chinkou_span <= 152.541 )
									ret := 0.101124
								if( chinkou_span > 152.541 )
									ret := 0.464819
						if( kinjun_sen > 150.478 )
							if( chinkou_span <= 154.836 )
								if( tenkan_sen <= 157.682 )
									ret := -0.174581
								if( tenkan_sen > 157.682 )
									ret := -0.533133
							if( chinkou_span > 154.836 )
								if( tenkan_sen <= 159.418 )
									ret := 0.278757
								if( tenkan_sen > 159.418 )
									ret := 0.020351
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Ichimoku_Cloud 
//@version=5
//indicator "Ichimoku Cloud", overlay=true)

// Input parameters for the Ichimoku Cloud
turning_periods = input.int(9, title="Tenkan-Sen Period")
standard_periods = input.int(26, title="Kinjun-Sen Period")
leading_span2_periods = input.int(52, title="Senkou Span B Period")
displacement = input.int(26, title="Displacement")

show_tenkan_sen = input.bool(true, title="Show Tenkan-Sen")
show_kinjun_sen = input.bool(true, title="Show Kinjun-Sen")
show_chinkou_span = input.bool(true, title="Show Chinkou Span")
show_cloud = input.bool(true, title="Show Cloud")
show_crosses = input.bool(false, title="Show Crosses")

// Donchian channel calculation
donchian(highs, lows, length) =>
    (ta.highest(highs, length) + ta.lowest(lows, length)) / 2

// Ichimoku calculations
tenkan_sen = donchian(high, low, turning_periods)
kinjun_sen = donchian(high, low, standard_periods)
senkou_span_a = (tenkan_sen + kinjun_sen) / 2
senkou_span_b = donchian(high, low, leading_span2_periods)

// Displaced Senkou Spans
senkou_span_a_displaced = senkou_span_a[displacement]
senkou_span_b_displaced = senkou_span_b[displacement]

// Chinkou Span
chinkou_span = close[displacement]

// Crosses
cross_up_tenkan_kinjun = ta.crossover(tenkan_sen, kinjun_sen)
cross_dn_tenkan_kinjun = ta.crossunder(tenkan_sen, kinjun_sen)
cross_up_tenkan_kinjunInt = cross_up_tenkan_kinjun ? 1 : 0  // Bool to int
cross_dn_tenkan_kinjunInt = cross_dn_tenkan_kinjun ? 1 : 0  // Bool to int

basis_minus = senkou_span_a - senkou_span_b
basis_max = senkou_span_a - tenkan_sen

// Plotting
plot(show_tenkan_sen ? tenkan_sen : na, color=color.lime, title="Tenkan-Sen", linewidth=1)
plot(show_kinjun_sen ? kinjun_sen : na, color=color.fuchsia, title="Kinjun-Sen", linewidth=1)
plot(show_chinkou_span ? chinkou_span : na, color=color.aqua, title="Chinkou Span", linewidth=1, offset=-displacement)

// Plot the Senkou Span lines and store the plot references
senkou_span_a_plot = plot(show_cloud ? senkou_span_a_displaced : na, color=color.green, title="Senkou Span A", linewidth=1)
senkou_span_b_plot = plot(show_cloud ? senkou_span_b_displaced : na, color=color.red, title="Senkou Span B", linewidth=1)

// Cloud filling
fill(senkou_span_a_plot, senkou_span_b_plot, color=color.new(color.lime, 90), title="Bullish Cloud", transp=70, fillgaps=true)
fill(senkou_span_a_plot, senkou_span_b_plot, color=color.new(color.red, 90), title="Bearish Cloud", transp=70, fillgaps=true)

plotshape(series=(show_crosses and cross_up_tenkan_kinjun) ? close : na, location=location.belowbar, color=color.yellow, style=shape.triangleup, size=size.small, title="Cross Up Tenkan Kinjun")
plotshape(series=(show_crosses and cross_dn_tenkan_kinjun) ? close : na, location=location.abovebar, color=color.yellow, style=shape.triangledown, size=size.small, title="Cross Down Tenkan Kinjun")

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
float op_operation = decision_tree_0_SOLUSDT_30Min_c54d1017(tenkan_sen, basis_minus, cross_up_tenkan_kinjunInt, senkou_span_a, cross_dn_tenkan_kinjunInt, senkou_span_b, chinkou_span, senkou_span_a_displaced, senkou_span_b_displaced, kinjun_sen, basis_max)

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


