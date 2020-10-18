<template>
  <div id="about">
    <h1 class="ml-3" style="font-weight:bold; text-align:left">Project g.o.t.c.h.a:</h1>
    <h2 class="ml-3 mb-3" style="color:#42b983; text-align:left">Government Observer: Transparency, Credibility and Honesty Application</h2>
    <b-row class="mb-5">
      <b-col style="border-right:1px solid black">
        <p class="ml-3" style="text-align:left;">Despite electing our politicians, the majority of citizens do not know how their own representatives vote, 
          nor the types of bills they even vote on. Despite the progression of technology, governmental legislation remains on outdated, non-intuitive databases 
          that deter any curious constituents. With g.o.t.c.h.a, we seek to change that. We strive to provide ease of access to legislation, breaking 
          down congressional bills into easy to digest summaries. More than that, transparency is our key, and we provide information on every senator 
          and representative pertaining to their voting record, communication outlets, sponsorships, and more, so that constituents can be better 
          informed of how their representatives are serving them. 
        </p>
      </b-col>
      <b-col>
        <h3 class="ml-2" style="text-align:left">Democracy cannot succeed unless those who express their choice are prepared to choose wisely. 
          The real safeguard of democracy, therefore, is education.</h3>
        <h2 class="ml-2" style="text-align:left; color:#42b983"> ~ Franklin Delano Roosevelt</h2>
      </b-col>
    </b-row>
    <h1 class="mt-5, mr-3" style="font-weight:bold; text-align:center">Meet Team B.L.U.E</h1>
    
    <b-row class="ml-3">

      <b-card-group deck class="mb-4, mx-auto">
        <b-row class="mt-4">
          <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
              <b-col md="6">
                <img src="../assets/reiden.jpg" class="card-img card-img-top img-fluid" />
              </b-col>
              <b-col md="6">
                <b-card-body title="Reiden Chea">
                  <b-card-text>
                    Reiden is a second year computer science major and math minor. He serves as the chair of 
                    Oversight within ASUW Senate, and when he's not breaking national records in powerlifting,
                    he enjoys 3D printing and making a good ol' bowl of oreo rice.
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
          <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
              <b-col md="6">
                <img src="../assets/jennifer.jpg" class="card-img card-img-top img-fluid" />
              </b-col>
              <b-col md="6">
                <b-card-body title="Jennifer Fernandez">
                  <b-card-text>
                    Jennifer -- but her best friends call her Jen -- is a sophomore majoring in computer science
                    and minoring in both physics and math. A talented and skilled figure skater, she was a 
                    top competitor in the national figure skating team of the Philipines.
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
        </b-row>
      </b-card-group>

      <b-card-group deck class="mb-4, mx-auto">
        <b-row class="mt-4">
          <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
              <b-col md="6">
                <img src="../assets/anson.jpg" class="card-img card-img-top img-fluid" />
              </b-col>
              <b-col md="6">
                <b-card-body title="Anson Huang">
                  <b-card-text>
                    Anson is a sophomore studying computer science and political science. He serves
                    as the chair of the Committee for Resolution Follow-Up within ASUW Senate. His hobbies
                    include running, basketball, and even cutting hair!
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
          <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
              <b-col md="6">
                <img src="../assets/huy.jpg" class="card-img card-img-top img-fluid" />
              </b-col>
              <b-col md="6">
                <b-card-body title="Huy Huynh">
                  <b-card-text>
                    Huy is a sophomore studying electrical engineering. He enjoys making things
                    out of nothing -- like a magician! To him, any sufficiently advanced technology
                    is nothing short of magic. His skills take him to Husky Robotics where he designed
                    a rover and RC car.
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
        </b-row>
      </b-card-group>

      <b-card-group deck class="mx-auto">
        <b-row class="mt-4">
          <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
              <b-col md="6">
                <img src="../assets/jared.jpg" class="card-img card-img-top img-fluid" />
              </b-col>
              <b-col md="6">
                <b-card-body title="Jared Tran">
                  <b-card-text>
                    Jared is a star. He's even in a program called STARS -- a rigorous program
                    for students from underprivileged backgrounds at the UW. When he's not pumping
                    iron, he is flying through weekly math problems and grinding to challenger 
                    in League of Legends.
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
        </b-row>
      </b-card-group>

    </b-row>

  </div>
</template>

<style>
#about {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.profiles {
  display: flex;
  flex-direction:column;
  width: 50%;
  height: 10%;
}

.profiles .img {
  flex: 2;
  border: 2px solid grey;
  height: 10%;
}

.profiles .text{
  flex: 6;
}
</style>
