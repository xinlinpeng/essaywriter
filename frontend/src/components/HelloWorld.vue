<template>
  <div class="hello">
    <div>
    <h1 class="essay_title">悟空策论</h1>
    <h2 class="sub_title">——懂你的中文议论文写作</h2>
    <form style="justify-content: space-between" class="ant-form ant-form-inline">
      <div style="margin:0 auto" >
        <el-row>
        <div class="h_and_tooltip">
          <h3>标题</h3>
        </div>
        <div class="h_and_tooltip">
          <el-tooltip class="item" effect="light" content="标题：只用于全文整合，不影响文本生成，可以不填。" placement="right-start">
            <i class="el-icon-question" />
          </el-tooltip>
        </div>
        </el-row>
        <el-row>
        <input type="text" v-model="title" placeholder="请输入主题" class="ant-input ant-input-lg essay_effectInput__18NjZ" style="width:600px;height:40px;border-radius:7px" value="" id="topic">
        </el-row>
        <div>
          <div style="width:60%;display: inline-block;float:left">
          <el-row>
          <div class="h_and_tooltip">
          <h3>分论点1</h3>
          </div>
          <div class="h_and_tooltip">
          <el-tooltip class="item" effect="light" content="分论点：生成文本的主要依据，也是段落的首句。如不填写，则不生成本段内容。" placement="right-start">
            <i class="el-icon-question" />
          </el-tooltip>
          </div>
          </el-row>
          <el-row>
          <input type="text" v-model="sub_title1" placeholder="请输入分论点" class="ant-input ant-input-lg essay_effectInput__18NjZ" style="width:340px;height:40px;border-radius:7px" value="" id="topic">
          </el-row>
          </div>
          <div style="width:40%;display: inline-block;float:left">
          <el-row>
          <div class="h_and_tooltip">
          <h3>关键词</h3>
          </div>
          <div class="h_and_tooltip">
          <el-tooltip class="item" effect="light" content="关键词：文本将围绕关键词展开，可能会在文中直接提及。可以不填，可以为多个，用空格隔开。" placement="right-start">
            <i class="el-icon-question" />
          </el-tooltip>
          </div>
          </el-row>
          <el-row>
          <input type="text" v-model="keyword1" placeholder="请输入该分论点下的关键词" class="ant-input ant-input-lg essay_effectInput__18NjZ" style="width:240px;height:40px;border-radius:7px" value="" id="topic">
          </el-row>
          </div>
        </div>
        <div>
          <div style="width:60%;display: inline-block;float:left">
          <h3>分论点2</h3>
          <input type="text" v-model="sub_title2" placeholder="请输入分论点" class="ant-input ant-input-lg essay_effectInput__18NjZ" style="width:340px;height:40px;border-radius:7px" value="" id="topic">
          </div>
          <div style="width:40%;display: inline-block;float:left">
          <h3>关键词</h3>
          <input type="text" v-model="keyword2" placeholder="请输入该分论点下的关键词" class="ant-input ant-input-lg essay_effectInput__18NjZ" style="width:240px;height:40px;border-radius:7px" value="" id="topic">
          </div>
        </div>
        <div>
          <div style="width:60%;display: inline-block;float:left">
          <h3>分论点3</h3>
          <input type="text" v-model="sub_title3" placeholder="请输入分论点" class="ant-input ant-input-lg essay_effectInput__18NjZ" style="width:340px;height:40px;border-radius:7px" value="" id="topic">
          </div>
          <div style="width:40%;display: inline-block;float:left">
          <h3>关键词</h3>
          <input type="text" v-model="keyword3" placeholder="请输入该分论点下的关键词" class="ant-input ant-input-lg essay_effectInput__18NjZ" style="width:240px;height:40px;border-radius:7px" value="" id="topic">
          </div>
        </div>
      </div>
    </form>
    <div id="father" style="text-align:center">
    <div style="margin-top:20px; ">
      <button style="margin-left:15px" type="button" class="but_ret" ant-click-animating-without-extra-node="false" @click="empty">
        <span>重置</span>
      </button>
      <!-- <button style="margin-left:15px" type="button" class="but_acc" @click="generate"> -->
        <button style="margin-left:15px" type="button" class="but_acc" @click="open">
        <span>生成</span>
      </button>
      <button style="margin-left:15px" type="button" class="but_ret" ant-click-animating-without-extra-node="false" @click="autowriter">
        <!-- @click="fix" -->
        <span>自动填写</span>
      </button>
      <el-tooltip class="item" effect="light" content="点击“自动填写”可以获得自动填写的多组分论点，选择并点击确定可以查看对应的已生成的缓存示例" placement="right-start">
        <i class="el-icon-question" />
      </el-tooltip>
      <el-dialog title="缓存结果" :visible.sync="dialogTableVisible" :append-to-body="true">
        <el-table :data="tableData" style="width: 100%; max-height:700px; margin-top:-20px" :highlight-current-row="true" @row-click="clickChange" height="300">
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left">
                <el-form-item label="论题：">
                  <span>{{ props.row.title }}</span>
                </el-form-item>
                <el-form-item label="分论点1：">
                  <span>{{ props.row.topic1 }}</span>
                </el-form-item>
                <el-form-item label="关键词：">
                  <span>{{ props.row.key1 }}</span>
                </el-form-item>
                <el-form-item label="分论点2：">
                  <span>{{ props.row.topic2 }}</span>
                </el-form-item>
                <el-form-item label="关键词：">
                  <span>{{ props.row.key2 }}</span>
                </el-form-item>
                <el-form-item label="分论点3：">
                  <span>{{ props.row.topic3 }}</span>
                </el-form-item>
                <el-form-item label="关键词：">
                  <span>{{ props.row.key2 }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column label="选择" width="55">
            <template slot-scope="scope">
                <el-radio  v-model="tableRadio" :label="scope.row"><i></i></el-radio>
            </template>
          </el-table-column>
          <el-table-column
            label="论题"
            align="center"
            prop="title">
          </el-table-column>
        </el-table>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" class="but_acc" @click="tableSelectAccept">确 定</el-button>
        </span>
      </el-dialog>
    </div>
    </div>
    <div v-if="isnotshow">
      <div class="h_and_tooltip" style="margin-left:20px">
        <h3>备选结果生成</h3>
        </div>
        <div class="h_and_tooltip">
        <el-tooltip class="item" effect="light" content="每段将生成两个备选结果，显示在下方，单击文本框，背景变为深蓝即表示选中该结果。" placement="right-start">
          <i class="el-icon-question" />
        </el-tooltip>
      </div>
    </div>
    <div v-if="isshow" class="essay_content__2xNIl">
      <div class="essay_empty__1ZGnW">
        <img src="../assets/search.png" style="width:100%;height: 200px;
      position: relative;margin-bottom:25px">
        <span>填写信息并开始生成...</span>
      </div>
    </div>
    <div v-if="isnotshow" style="margin-top:0px;height:auto;">
      <div class="carousel-wrap" style="margin-top:0px;height:auto;">
        <!-- 轮播图第一段 -->

        <el-carousel style="height:auto;" :interval="0">
          <!-- <el-carousel-item v-for="item in bannerList" :key="item.id">
            <div id="inner" contenteditable="true" style="height:auto;">
              <h3>{{ item.text }}</h3>
            </div>
          </el-carousel-item> -->
          <div class="div_car1">
          <el-carousel-item style="height:auto;" :class="select1_1?'hover':''">
            <el-alert
              v-if="success1_1"
              title="段落一备选结果（1）生成成功"
              type="success"
              show-icon>
            </el-alert>
            <el-alert
              v-if="api_num"
              title="今日接口次数已用尽，请明日再试"
              type="warning"
              show-icon>
            </el-alert>
            <el-alert
              v-if="fail1_1"
              title="服务器压力较大，生成失败"
              type="error"
              description="请点击下方刷新按钮重新生成（或稍后重新生成结果）"
              close-text="刷新"
              @close="reload1_1"
              show-icon>
            </el-alert>
            <div style="margin:40px;height:auto;min-height:200px" @click="check1_1" v-loading=loading1_1>
              <div style="margin-left:80px;margin-right:80px">
              <span style="font-size:18px;min-height:200px;width:100;margin:20px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{section1_1}}</span>
              </div>
            </div>
          </el-carousel-item>
          </div>
          <el-carousel-item style="height:auto;" :class="select1_2?'hover':''">
            <el-alert
              v-if="success1_2"
              title="段落一备选结果（2）生成成功"
              type="success"
              show-icon>
            </el-alert>
            <el-alert
              v-if="api_num"
              title="今日接口次数已用尽，请明日再试"
              type="warning"
              show-icon>
            </el-alert>
            <el-alert
              v-if="fail1_2"
              title="服务器压力较大，生成失败"
              type="error"
              description="请点击下方刷新按钮重新生成（或稍后重新生成结果）"
              close-text="刷新"
              @close="reload1_2"
              show-icon>
            </el-alert>
            <div style="margin:40px;min-height:200px" @click="check1_2" v-loading=loading1_2>
              <div style="margin-left:80px;margin-right:80px">
              <span style="font-size: 18px;min-height:200px;width:100;margin:20px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{section1_2}}</span>
              </div>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
      <div class="carousel-wrap" style="margin-top:10px;height:auto;">
        <!-- 轮播图第二段 -->
        <el-carousel style="height:auto;" :interval="0">
          <el-carousel-item style="height:auto;" :class="select2_1?'hover':''">
            <el-alert
              v-if="success2_1"
              title="段落二备选结果（1）生成成功"
              type="success"
              show-icon>
            </el-alert>
            <el-alert
              v-if="api_num"
              title="今日接口次数已用尽，请明日再试"
              type="warning"
              show-icon>
            </el-alert>
            <el-alert
              v-if="fail2_1"
              title="服务器压力较大，生成失败"
              type="error"
              description="请点击下方刷新按钮重新生成（或稍后重新生成结果）"
              close-text="刷新"
              @close="reload2_1"
              show-icon>
            </el-alert>
            <div style="margin:40px;min-height:200px" @click="check2_1" v-loading=loading2_1>
              <div style="margin-left:80px;margin-right:80px">
              <span style="font-size: 18px;min-height:200px;width:100;margin:20px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{section2_1}}</span>
              </div>
            </div>
          </el-carousel-item>
          <el-carousel-item style="height:auto;" :class="select2_2?'hover':''">
            <el-alert
              v-if="success2_2"
              title="段落二备选结果（2）生成成功"
              type="success"
              show-icon>
            </el-alert>
            <el-alert
              v-if="api_num"
              title="今日接口次数已用尽，请明日再试"
              type="warning"
              show-icon>
            </el-alert>
            <el-alert
              v-if="fail2_2"
              title="服务器压力较大，生成失败"
              type="error"
              description="请点击下方刷新按钮重新生成（或稍后重新生成结果）"
              close-text="刷新"
              @close="reload2_2"
              show-icon>
            </el-alert>
            <div style="margin:40px;min-height:200px" @click="check2_2" v-loading=loading2_2>
              <div style="margin-left:80px;margin-right:80px">
              <span style="font-size: 18px;min-height:200px;width:100;margin:20px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{section2_2}}</span>
              </div>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
      <div class="carousel-wrap" style="margin-top:10px;height:auto;">
        <!-- 轮播图第三段 -->
        <el-carousel style="height:auto;" :interval="0">
          <el-carousel-item style="height:auto" :class="select3_1?'hover':''">
            <el-alert
              v-if="success3_1"
              title="段落三备选结果（1）生成成功"
              type="success"
              show-icon>
            </el-alert>
            <el-alert
              v-if="api_num"
              title="今日接口次数已用尽，请明日再试"
              type="warning"
              show-icon>
            </el-alert>
            <el-alert
              v-if="fail3_1"
              title="服务器压力较大，生成失败"
              type="error"
              description="请点击下方刷新按钮重新生成（或稍后重新生成结果）"
              close-text="刷新"
              @close="reload3_1"
              show-icon>
            </el-alert>
            <div style="margin:40px;min-height:200px" @click="check3_1" v-loading=loading3_1>
              <div style="margin-left:80px;margin-right:80px">
              <span style="font-size: 18px;min-height:200px;width:100;margin:20px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{section3_1}}</span>
              </div>
            </div>
          </el-carousel-item>
          <el-carousel-item style="height:auto" :class="select3_2?'hover':''">
            <el-alert
              v-if="success3_2"
              title="段落三备选结果（2）生成成功"
              type="success"
              show-icon>
            </el-alert>
            <el-alert
              v-if="api_num"
              title="今日接口次数已用尽，请明日再试"
              type="warning"
              show-icon>
            </el-alert>
            <el-alert
              v-if="fail3_2"
              title="服务器压力较大，生成失败"
              type="error"
              description="请点击下方刷新按钮重新生成（或稍后重新生成结果）"
              close-text="刷新"
              @close="reload3_2"
              show-icon>
            </el-alert>
            <div style="margin:40px;min-height:200px" @click="check3_2" v-loading=loading3_2>
              <div style="margin-left:80px;margin-right:80px">
              <span style="font-size: 18px;min-height:200px;width:100;margin:20px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{section3_2}}</span>
              </div>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
    <div style="margin:20px;text-align: center" v-if="allbuttonshow">
      <button style="margin-left:15px" type="button" class="but_acc" @click="showallessay">
        <span>全文生成</span>
      </button>
      <el-tooltip class="item" effect="light" content="每段选定一个结果后，单击全文生成，各段将整合在文本编辑器中，可以进行编辑。" placement="right-start">
        <i class="el-icon-question" />
      </el-tooltip>
    </div>
    <div v-show="essayisshow" style="margin-top:20px;padding-top:20px;padding-bottom:20px;height:auto;background-color: #CDE0EA">
      <div style="margin-left:20px;margin-right:20px;padding-top:20px;padding-bottom:20px;height:auto;background-color:#ffff;">
        <div style="text-align: center" v-if="loading">
        <img src="../assets/load.gif" style="align-items:center;">
        </div>
        <!-- <div style="text-align: center;margin-bottom:15px">
          <h3 style="font-size: 25px;margin:0 auto;font-family:宋体">{{new_title}}</h3>
        </div> -->
        <div id="div1">
          <div id="printTest">
          <!-- <span style="font-size: 18px;height:100;width:100;margin:20px;line-height:30pt;font-family:宋体">{{final_text}}</span> -->
          <div style="text-align: center;margin-bottom:15px;margin-top:15px;">
          <span style="text-align: center;font-size: 25px;margin:0 auto;font-family:宋体">{{new_title}}</span>
          </div>
          <div>
          <span style="font-size: 18px;height:100;width:100;margin:20px;margin-left:80px;margin-right:80px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{text1}}</span>
          </div>
          <div>
          <span style="font-size: 18px;height:100;width:100;margin:20px;margin-left:80px;margin-right:80px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{text2}}</span>
          </div>
          <div>
          <span style="font-size: 18px;height:100;width:100;margin:20px;margin-left:80px;margin-right:80px;line-height:30pt;font-family:宋体;display:block;text-indent:2em;">{{text3}}</span>
          </div>
          </div>
        </div>
      </div>
      <div style="margin:20px;text-align: center" v-if="allbuttonshow">
      <button style="margin-left:15px" type="button" class="but_ret" @click="downloadessay">
        <span>文章导出</span>
      </button>
      <button style="margin-left:15px" type="button" class="but_acc" v-print="'#printTest'">PDF打印</button>
    </div>
    </div>
    </div>
    <!-- <div> -->

    <!-- </div> -->
  </div>
</template>

<script>
/* eslint-disable */
const axios = require('axios');
// import {get} from "../utils/communication"
import API from "../utils/API";
import E from 'wangeditor';
import { quillEditor } from 'vue-quill-editor';
import cachedata from '@/assets/cache_new.json'
export default {
  name: 'HelloWorld',
  data () {
    return {
      title: '',
      sub_title1: '',
      keyword1: '',
      sub_title2: '',
      keyword2: '',
      sub_title3: '',
      keyword3: '',
      isshow: true,
      isnotshow: false,
      essayisshow: false,
      loading: false,
      bannerList: [
        { id: 0, text: '高尔基说过：“(开头)好像音乐里定调一样，全曲的音调都是它给予的，也是作者花功夫的所在。”议论文的开头要讲究“短、快、靓”。短，即要简捷，最好三两句成段，引入本论。开头短，可避免冗长之赘，而且短句成段，在空间上突出其内容的重要性。快，即入题要快，最好三言两语就点明文章的基本观点或议论的话题。因为评分标准中有“中心明确”的细则。开篇确定中心，有利于阅卷者按等计分，也有利于作者展开论述，不致出现主旨不清、中途转换论题等作文大忌。靓，即要精彩。这也是传统文论中所说的“凤头”。精彩的开头，最突出的效果是吸引阅卷者，给阅卷者留下好的印象。文章开头要精彩，多用比喻、类比、排比等修辞引入论点，还可引述名言，讲述寓言故事导入话题。' },
        { id: 1, text: '高尔基说过：“(开头)好像音乐里定调一样，全曲的音调都是它给予的，也是作者花功夫的所在。”议论文的开头要讲究“短、快、靓”。短，即要简捷，最好三两句成段，引入本论。开头短，可避免冗长之赘，而且短句成段，在空间上突出其内容的重要性。快，即入题要快，最好三言两语就点明文章的基本观点或议论的话题。因为评分标准中有“中心明确”的细则。开篇确定中心，有利于阅卷者按等计分，也有利于作者展开论述，不致出现主旨不清、中途转换论题等作文大忌。靓，即要精彩。这也是传统文论中所说的“凤头”。精彩的开头，最突出的效果是吸引阅卷者，给阅卷者留下好的印象。文章开头要精彩，多用比喻、类比、排比等修辞引入论点，还可引述名言，讲述寓言故事导入话题。' },
      ],
      // height:'500px',
      // autoheight: '400',
      new_title: '',
      text0: '\n\n\n\n',
      text1: '',
      text2: '',
      text3: '',
      final_text: '',
      section1_1: 'sec1-1',
      section1_2: 'sec1-2',
      loading1_1: false,
      loading1_2: false,
      section2_1: 'sec2-1',
      section2_2: 'sec2-2',
      loading2_1: false,
      loading2_2: false,
      section3_1: 'sec3-1',
      section3_2: 'sec3-2',
      loading3_1: false,
      loading3_2: false,
      notloading3_1: false,
      notloading3_2: false,
      allbuttonshow: false,
      api_num: false,
      success1_1: false,
      fail1_1: false,
      success1_2: false,
      fail1_2: false,
      success2_1: false,
      fail2_1: false,
      success2_2: false,
      fail2_2: false,
      success3_1: false,
      fail3_1: false,
      success3_2: false,
      fail3_2: false,
      select1_1: false,
      select1_2: false,
      select2_1: false,
      select2_2: false,
      select3_1: false,
      select3_2: false,
      select1: '',
      select2: '',
      select3: '',
      content: '',
      editor: undefined,
      tableData: [],
      dialogTableVisible: false,
      tableRadio: '',
      result: '',
    }
  },
  // beforeMount:function(){
  //   var height=$("#inner").height();
  //   this.autoheight = (height+60) + 'px';
  // },
  methods: {
    open() {
        this.$confirm('生成会耗时约3到5分钟，您可以选择自动填写查看已缓存内容或者选择继续使用预训练模型生成, 是否继续生成?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '已为您继续生成'
          });
          this.generate()
          this.openVn()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消生成，您可以点击全文生成查看历史缓存生成文章'
          });
        });
      },
    openVn() {
        const h = this.$createElement;
        this.$message({
          message: h('p', null, [
            h('span', null, '下拉查看生成内容'),
          ]),
          center: true
        });
      },
    open_success(string) {
        this.$message({
          showClose: true,
          message: string + '生成成功',
          type: 'success'
        });
      },
    downloadessay(){
      let data = this.editor.txt.html();
      console.log("导出文章")
      console.log(data)
      this.result = this.new_title + '\n' + this.text1 + '\n' + this.text2 + '\n' + this.text3 + '\n'
      var FileSaver = require('file-saver');
      var blob = new Blob([data], {type: "text/plain;charset=utf-8"});
      FileSaver.saveAs(blob, this.new_title + ".docx");
    },
    empty () {
      this.title = ''
      this.sub_title1 = ''
      this.sub_title2 = ''
      this.sub_title3 = ''
      this.keyword1 = ''
      this.keyword2 = ''
      this.keyword3 = ''
      this.isshow = true
      this.isnotshow = false
      this.essayisshow = false
      this.loading = false
      this.allbuttonshow = false
      this.tableRadio = ''
    },
    tableSelectAccept(){
      this.openVn()
      this.dialogTableVisible = false
      this.essayisshow = false
      this.isshow = false
      this.isnotshow = true
      this.loading1_1 = true
      this.loading1_2 = true
      this.loading2_1 = true
      this.loading2_2 = true
      this.loading3_1 = true
      this.loading3_2 = true
      // this.new_title = this.title
      this.select1_1 = false
      this.select1_2 = false
      this.select2_1 = false
      this.select2_2 = false
      this.select3_1 = false
      this.select3_2 = false
      this.section1_1 = this.section1_2 = this.section2_1 = this.section2_2 = this.section3_1 = this.section3_2 = ''
      this.text1 = this.text2 = this.text3 = ''
      this.new_title = this.title
      this.allbuttonshow = true
      // console.log(this.tableRadio)
      var ids = []
      for(var i = 0; i < this.tableRadio['id1'].length; i++){
        ids.push(this.tableRadio['id1'][i])
      }
      for(var i = 0; i < this.tableRadio['id2'].length; i++){
        ids.push(this.tableRadio['id2'][i])
      }
      for(var i = 0; i < this.tableRadio['id3'].length; i++){
        ids.push(this.tableRadio['id3'][i])
      }
      console.log(ids)
      this.section1_1 = this.tableRadio['para1_1']
      this.loading1_1 = false
      this.success1_1 = true
      this.fail1_1 = false
      this.section1_2 = this.tableRadio['para1_2']
      this.loading1_2 = false
      this.success1_2 = true
      this.fail1_2 = false
      this.section2_1 = this.tableRadio['para2_1']
      this.loading2_1 = false
      this.success2_1 = true
      this.fail2_1 = false
      this.section2_2 = this.tableRadio['para2_2']
      this.loading2_2 = false
      this.success2_2 = true
      this.fail2_2 = false
      this.section3_1 = this.tableRadio['para3_1']
      this.loading3_1 = false
      this.success3_1 = true
      this.fail3_1 = false
      this.section3_2 = this.tableRadio['para3_2']
      this.loading3_2 = false
      this.success3_2 = true
      this.fail3_2 = false
    },
    autowriter(){
      this.dialogTableVisible = true
      // console.log(cachedata)
      if(this.tableData.length == 0){
        for(var i = 0; i < cachedata.length; i++){
        var data_tmp = {}
        data_tmp['title'] = cachedata[i].title
        data_tmp['topic1'] = cachedata[i].argument[0].topic
        data_tmp['key1'] = ''
        for(var k = 0; k < cachedata[i].argument[0].keyword.length; k++){
          data_tmp['key1'] += cachedata[i].argument[0].keyword[k] + " "
        }
        data_tmp['topic2'] = cachedata[i].argument[1].topic
        data_tmp['key2'] = ''
        for(var k = 0; k < cachedata[i].argument[1].keyword.length; k++){
          data_tmp['key2'] += cachedata[i].argument[1].keyword[k] + " "
        }
        data_tmp['topic3'] = cachedata[i].argument[2].topic
        data_tmp['key3'] = ''
        for(var k = 0; k < cachedata[i].argument[2].keyword.length; k++){
          data_tmp['key3'] += cachedata[i].argument[2].keyword[k] + " "
        }
        data_tmp['id1'] = cachedata[i].argument[0].id
        data_tmp['id2'] = cachedata[i].argument[1].id
        data_tmp['id3'] = cachedata[i].argument[2].id
        data_tmp['para1_1'] = cachedata[i].argument[0].para1
        data_tmp['para1_2'] = cachedata[i].argument[0].para2
        data_tmp['para2_1'] = cachedata[i].argument[1].para1
        data_tmp['para2_2'] = cachedata[i].argument[1].para2
        data_tmp['para3_1'] = cachedata[i].argument[2].para1
        data_tmp['para3_2'] = cachedata[i].argument[2].para2
        this.tableData.push(data_tmp)
      }
      }
    },
    check1_1(){
      console.log("check 1_1")
      this.select1_1 = true
      this.select1_2 = false
      this.text1 = this.section1_1
      // this.select1 = this.section1_1
    },
    check1_2(){
      console.log("check 1_2")
      this.select1_2 = true
      this.select1_1 = false
      this.text1 = this.section1_2
      // this.select1 = this.section1_2
    },
    check2_1(){
      console.log("check 2_1")
      this.select2_1 = true
      this.select2_2 = false
      this.text2 = this.section2_1
      // this.select2 = this.section2_1
    },
    check2_2(){
      console.log("check 2_2")
      this.select2_2 = true
      this.select2_1 = false
      this.text2 = this.section2_2
      // this.select2 = this.section2_2
    },
    check3_1(){
      console.log("check 3_1")
      this.select3_1 = true
      this.select3_2 = false
      this.text3 = this.section3_1
      // this.select3 = this.section3_1
    },
    check3_2(){
      console.log("check 3_2")
      this.select3_2 = true
      this.select3_1 = false
      this.text3 = this.section3_2
      // this.select3 = this.section3_2
    },
    reload1_1(){
      console.log("reload 1_1")
      this.paragraph_1_1()
    },
    reload1_2(){
      console.log("reload 1_2")
      this.paragraph_1_2()
    },
    reload2_1(){
      console.log("reload 2_1")
      this.paragraph_2_1()
    },
    reload2_2(){
      console.log("reload 2_2")
      this.paragraph_2_2()
    },
    reload3_1(){
      console.log("reload 3_1")
      this.paragraph_3_1()
    },
    reload3_2(){
      console.log("reload 3_2")
      this.paragraph_3_2()
    },
    generate () {
      this.essayisshow = false
      this.isshow = false
      this.isnotshow = true
      this.allbuttonshow = true
      this.success1_1 = false
      this.success1_2 = false
      this.success2_1 = false
      this.success2_2 = false
      this.success3_1 = false
      this.success3_2 = false
      this.fail1_1 = false
      this.fail1_2 = false
      this.fail2_1 = false
      this.fail2_2 = false
      this.fail3_1 = false
      this.fail3_2 = false
      this.select1_1 = false
      this.select1_2 = false
      this.select2_1 = false
      this.select2_2 = false
      this.select3_1 = false
      this.select3_2 = false
      this.section1_1 = this.section1_2 = this.section2_1 = this.section2_2 = this.section3_1 = this.section3_2 = ''
      this.text1 = this.text2 = this.text3 = ''
      this.paragraph_1()
      this.paragraph_2()
      this.paragraph_3()
    },
    paragraph_1_1(){
      this.loading1_1 = true
      this.notloading1_1 = false
      var _topic1_1 = null
      var _keyword1_1 = null
      if(this.sub_title1 != ''){
        _topic1_1 = this.sub_title1
        _keyword1_1 = this.keyword1
      }
      if(this.sub_title1 == "失败是成功之母。"){
        _topic1_1 = '1'+this.sub_title1
        _keyword1_1 = this.keyword1
      }
      console.log(_topic1_1)
      console.log(_keyword1_1)
      axios.get(API.GET_ESSAYLIST.path
      ,{
        params : {
          topic:_topic1_1,
          keyword:_keyword1_1
        }
      }
      ).then((res) =>{
        console.log(res)
        this.section1_1 = res.data.result
        this.notloading1_1 = true
        this.loading1_1 = false
        this.success1_1 = true
        this.fail1_1 = false
        if(res.data.error_num == 2)
          this.api_num = true
        this.open_success("第一段备选结果一")
      }, (err) =>{
        console.log(err)
        this.loading1_1 = false
        this.success1_1 = false
        this.fail1_1 = true
      })
    },
    paragraph_1_2(){
      this.loading1_2 = true
      this.notloading1_2 = false
      var _topic1_2 = null
      var _keyword1_2 = null
      if(this.sub_title1 != ''){
        _topic1_2 = this.sub_title1
        _keyword1_2 = this.keyword1
      }
      if(this.sub_title1 == "失败是成功之母。"){
        _topic1_2 = '2'+this.sub_title1
        _keyword1_2 = this.keyword1
      }
      axios.get(API.GET_ESSAYLIST.path
      ,{
        params : {
          topic:_topic1_2,
          keyword:_keyword1_2
        }
      }
      ).then((res) =>{
        console.log(res)
        this.section1_2 = res.data.result
        this.notloading1_2 = true
        this.loading1_2 = false
        this.success1_2 = true
        this.fail1_2 = false
        if(res.data.error_num == 2)
          this.api_num = true
        this.open_success("第一段备选结果二")
      }, (err) =>{
        console.log(err)
        this.loading1_2 = false
        this.success1_2 = false
        this.fail1_2 = true
      })
    },
    paragraph_1(){
      this.paragraph_1_1()
      this.paragraph_1_2()
    },
    paragraph_2_1(){
      this.loading2_1 = true
      this.notloading2_1 = false
      var _topic2_1 = null
      var _keyword2_1 = null
      if(this.sub_title2 != ''){
        _topic2_1 = this.sub_title2
        _keyword2_1 = this.keyword2
      }
      if(this.sub_title2 == "通过失败积攒的经验,最终会成为走向成功的基石。"){
        _topic2_1 = '1'+this.sub_title2
        _keyword2_1 = this.keyword2
      }
      console.log(_topic2_1)
      console.log(_keyword2_1)
      axios.get(API.GET_ESSAYLIST.path
      ,{
        params : {
          topic:_topic2_1,
          keyword:_keyword2_1
        }
      }
      ).then((res) =>{
        console.log(res)
        this.section2_1 = res.data.result
        this.notloading2_1 = true
        this.loading2_1 = false
        this.success2_1 = true
        this.fail2_1 = false
        if(res.data.error_num == 2)
          this.api_num = true
        this.open_success("第二段备选结果一")
      }, (err) =>{
        console.log(err)
        this.loading2_1 = false
        this.success2_1 = false
        this.fail2_1 = true
      })
    },
    paragraph_2_2(){
      this.loading2_2 = true
      this.notloading2_2 = false
      var _topic2_2 = null
      var _keyword2_2 = null
      if(this.sub_title2 != ''){
        _topic2_2 = this.sub_title2
        _keyword2_2 = this.keyword2
      }
      if(this.sub_title2 == "通过失败积攒的经验,最终会成为走向成功的基石。"){
        _topic2_2 = '2'+this.sub_title2
        _keyword2_2 = this.keyword2
      }
      console.log(_topic2_2)
      console.log(_keyword2_2)
      axios.get(API.GET_ESSAYLIST.path
      ,{
        params : {
          topic:_topic2_2,
          keyword:_keyword2_2
        }
      }
      ).then((res) =>{
        console.log(res)
        this.section2_2 = res.data.result
        this.notloading2_2 = true
        this.loading2_2 = false
        this.success2_2 = true
        this.fail2_2 = false
        if(res.data.error_num == 2)
          this.api_num = true
        this.open_success("第二段备选结果二")
      }, (err) =>{
        console.log(err)
        this.loading2_2 = false
        this.success2_2 = false
        this.fail2_2 = true
      })
    },
    paragraph_2(){
      this.paragraph_2_1()
      this.paragraph_2_2()
    },
    paragraph_3_1(){
      this.loading3_1 = true
      this.notloading3_1 = false
      var _topic3_1 = null
      var _keyword3_1 = null
      if(this.sub_title3 != ''){
        _topic3_1 = this.sub_title3
        _keyword3_1 = this.keyword3
      }
      if(this.sub_title3 == "正确看待成功与失败,不要因为成功自满,也不要因为失败气馁。"){
        _topic3_1 = '1'+this.sub_title3
        _keyword3_1 = this.keyword3
      }
      console.log(_topic3_1)
      console.log(_keyword3_1)
      axios.get(API.GET_ESSAYLIST.path
      ,{
        params : {
          topic:_topic3_1,
          keyword:_keyword3_1
        }
      }
      ).then((res) =>{
        console.log(res)
        this.section3_1 = res.data.result
        this.notloading3_1 = true
        this.loading3_1 = false
        this.success3_1 = true
        this.fail3_1 = false
        if(res.data.error_num == 2)
          this.api_num = true
        this.open_success("第三段备选结果一")
      }, (err) =>{
        console.log(err)
        this.loading3_1 = false
        this.success3_1 = false
        this.fail3_1 = true
      })
    },
    paragraph_3_2(){
      this.loading3_2 = true
      this.notloading3_2 = false
      var _topic3_2 = null
      var _keyword3_2 = null
      if(this.sub_title3 != ''){
        _topic3_2 = this.sub_title3
        _keyword3_2 = this.keyword3
      }
      if(this.sub_title3 == "正确看待成功与失败,不要因为成功自满,也不要因为失败气馁。"){
        _topic3_2 = '2'+this.sub_title3
        _keyword3_2 = this.keyword3
      }
      console.log(_topic3_2)
      console.log(_keyword3_2)
      axios.get(API.GET_ESSAYLIST.path
      ,{
        params : {
          topic:_topic3_2,
          keyword:_keyword3_2
        }
      }
      ).then((res) =>{
        console.log(res)
        this.section3_2 = res.data.result
        this.notloading3_2 = true
        this.loading3_2 = false
        this.success3_2 = true
        this.fail3_2 = false
        if(res.data.error_num == 2)
          this.api_num = true
        this.open_success("第三段备选结果二")
      }, (err) =>{
        console.log(err)
        this.loading3_2 = false
        this.success3_2 = false
        this.fail3_2 = true
      })
    },
    paragraph_3(){
      this.paragraph_3_1()
      this.paragraph_3_2()
    },
    create (topic, keyword) {
      var _topic = null
      var _keyword = null
      if(topic != '' && keyword != ''){
        _topic = topic
        _keyword = keyword
      }
      console.log(_topic)
      console.log(_keyword)
      axios.get(API.GET_ESSAYLIST.path
      ,{
        params : {
          topic:_topic,
          keyword:_keyword
        }
      }
      ).then((res) =>{
        console.log(res)
        this.text1 = res.result
      },(err) => {
        console.log(err)
      })
    },
    showallessay(){
      this.openVn()
      if(this.editor == undefined){
        this.editor = new E('#div1')
        this.editor.config.height = 800
        this.editor.create()
      }
      // const editor = new E('#div1')
      // this.final_text = this.text1 + '\r\n'+ this.text2 + '\r\n'+ this.text3
      // // 配置 onchange 回调函数
      // // editor.config.onchange = function (newHtml) {
      // //   console.log('change 之后最新的 html', newHtml)
      // // }
      // editor.config.height = 600
      // editor.create()
      this.new_title = this.title
      // this.text1 = this.select1
      // this.text2 = this.select2
      // this.text3 = this.select3
      this.content= this.text1 + '\r\n'+ this.text2 + '\r\n'+ this.text3
      this.essayisshow = true
    },
    fix(){
      this.title = "论成败"
      this.sub_title1 = "失败是成功之母。"
      this.sub_title2 = "通过失败积攒的经验,最终会成为走向成功的基石。"
      this.keyword2 = "失败经验"
      this.sub_title3 = "正确看待成功与失败,不要因为成功自满,也不要因为失败气馁。"
      this.keyword3 = "看待成败"
    },
    check () {

    },
    clickChange (item) {
      this.tableRadio = item
      console.log(this.tableRadio)
      this.title = item.title
      this.sub_title1 = item.topic1
      this.sub_title2 = item.topic2
      this.sub_title3 = item.topic3
      this.keyword1 = item.key1
      this.keyword2 = item.key2
      this.keyword3 = item.key3
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
  text-align: center;
  size: 20px;
  color: #B6A38D;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.essay_title {
    font-size: 4rem;
    margin-bottom: 32px;
    font-family: "宋体";
    letter-spacing: .1em;
    color: #b6a38d;
    text-align: center;
    font-weight: bold;
}
.sub_title {
    font-family: "宋体";
    font-weight: bold;
}
h3 {
    display: block;
    font-size: 1.17em;
    margin-block-start: 0.5em;
    margin-block-end: 0.5em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    /* font-weight: bold; */
}
element.style {
    justify-content: space-between;
}
.ant-form {
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    color: rgba(0,0,0,.85);
    font-size: 14px;
    font-variant: tabular-nums;
    line-height: 1.5715;
    list-style: none;
    -moz-font-feature-settings: "tnum","tnum";
    font-feature-settings: "tnum","tnum";
}
.ant-form-inline {
    display: -webkit-flex;
    display: -moz-box;
    display: flex;
    -webkit-flex-wrap: wrap;
    flex-wrap: wrap;
}
.ant-form-item {
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    padding: 0;
    color: rgba(0,0,0,.85);
    font-size: 14px;
    font-variant: tabular-nums;
    line-height: 1.5715;
    list-style: none;
    -moz-font-feature-settings: "tnum","tnum";
    font-feature-settings: "tnum","tnum";
    margin: 0 0 24px;
    vertical-align: top;
}
.ant-row {
    display: -webkit-flex;
    display: -moz-box;
    display: flex;
    -webkit-flex-flow: row wrap;
    -moz-box-orient: horizontal;
    -moz-box-direction: normal;
    flex-flow: row wrap;
}
.ant-col {
    position: relative;
    max-width: 100%;
    min-height: 1px;
}
.ant-form-item-control-input {
    min-height: auto;
}
.ant-input:placeholder-shown {
    text-overflow: ellipsis;
}
.essay_effectInput__18NjZ {
    box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
}
.ant-input-lg {
    padding: 6.5px 11px;
    font-size: 16px;
}
.ant-input {
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    margin: 0;
    font-variant: tabular-nums;
    list-style: none;
    -moz-font-feature-settings: "tnum","tnum";
    font-feature-settings: "tnum","tnum";
    position: relative;
    display: inline-block;
    width: 100%;
    min-width: 0;
    padding: 4px 11px;
    color: rgba(0,0,0,.85);
    font-size: 14px;
    line-height: 1.5715;
    background-color: #fff;
    background-image: none;
    border: 1px solid #d9d9d9;
    border-radius: 2px;
    -moz-transition: all .3s;
    transition: all .3s;
}
.but_ret {
    background: #b6a38d;
    border-color: #b6a38d;
    color: #fff;
    line-height: 1.5715;
    position: relative;
    display: inline-block;
    font-weight: 400;
    white-space: nowrap;
    text-align: center;
    background-image: none;
    box-shadow: 0 2px 0 rgba(0,0,0,.015);
    cursor: pointer;
    -moz-transition: all .3s cubic-bezier(.645,.045,.355,1);
    transition: all .3s cubic-bezier(.645,.045,.355,1);
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    touch-action: manipulation;
    height: 32px;
    padding: 4px 15px;
    font-size: 14px;
    border-radius: 2px;
    border: 1px solid #d9d9d9;
}
.but_acc {
    background: #7e96b0;
    border-color: #7e96b0;
    color: #fff;
    line-height: 1.5715;
    position: relative;
    display: inline-block;
    font-weight: 400;
    white-space: nowrap;
    text-align: center;
    background-image: none;
    box-shadow: 0 2px 0 rgba(0,0,0,.015);
    cursor: pointer;
    -moz-transition: all .3s cubic-bezier(.645,.045,.355,1);
    transition: all .3s cubic-bezier(.645,.045,.355,1);
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    touch-action: manipulation;
    height: 32px;
    padding: 4px 15px;
    font-size: 14px;
    border-radius: 2px;
    border: 1px solid #d9d9d9;
}
.essay_content__2xNIl {
    width: "100%";
    height: 417px;
    position: relative;
    margin-block: 50px;
    /* background: #fff; */
    border-radius: 7px;
    box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
}
.essay_empty__1ZGnW {
    width: 200px;
    position: absolute;
    left: 50%;
    top: 50%;
    -webkit-transform: translate(-50%,-50%);
    -moz-transform: translate(-50%,-50%);
    transform: translate(-50%,-50%);
    font-size: 15px;
    letter-spacing: 2px;
    color: #aaa9a9;
}
.el-carousel__item{
  width: 100%;
  background-color: #d3dce6;
}
.el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    text-align: center;
    opacity: 0.75;
    line-height: 40px;
    margin: 30px;
}
.el-carousel__item.hover{
  background-color: #99a9bf;
}

.tips{
  background: #EFF4F8;
  background-color: #EFF4F8;
}
.el-collapse-item{
  background: #EFF4F8;
  background-color: #EFF4F8;
}
.demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
  .el-table-filter {
    max-height: 300px;
    overflow: auto;
}
.el-form-item{
    margin-bottom: 0px;
}
.h_and_tooltip{
  display: inline-block;
}

</style>
