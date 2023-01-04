# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 21:05:23 2022
LAKERS PLOTS
@author: ericd
"""

############################################## LAKERS PLOT ###############################

lakers = pd.read_csv('lakersPerGame.csv')

lakers.head()

lakersShooting = pd.read_csv('lakersShooting.csv')
lakersShooting.head()

lakers = pd.merge(lakers, lakersShooting, on=['Player'])

lakers = lakers[lakers.Player != 'Isaiah Thomas']
lakers = lakers[lakers.Player != 'Darren Collison']
lakers = lakers[lakers.Player != 'Chaundee Brown Jr.']
lakers = lakers[lakers.Player != 'Sekou Doumbouya']
lakers = lakers[lakers.Player != 'Jemerrio Jones']
lakers = lakers[lakers.Player != 'Mason Jones']

#add path column
lakers['path'] = 'C:/Users/ericd/OneDrive - North Carolina State University/Desktop/PersonalProjects/Lakers/Headshots/'+ lakers['Player']  + '.png'


#headshots
def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.16, alpha=1)


#mid range percentage FGA and FG% plot
fig, ax = plt.subplots(figsize=(6, 4), dpi=600)
ax.scatter(lakers['10-16Perc'],lakers['10-16Att'], color='white')
ax.set_title('Mid-Range Shooting, Los Angeles Lakers, 2022', size=10)
ax.set_ylabel('Percent of shots taken that are midrange')
ax.set_xlabel('Midrange shooting percentage')



for index, row in lakers.iterrows():
    ab = AnnotationBbox(getImage(row['path']), (row['10-16Perc'], row['10-16Att']), frameon=False)
    ax.add_artist(ab)
